import os
import tensorrt as trt

TRT_LOGGER = trt.Logger()


def get_engine(engine_file_path):
    print("Reading engine from file {}".format(engine_file_path))
    with open(engine_file_path, "rb") as f, trt.Runtime(TRT_LOGGER) as runtime:
        return runtime.deserialize_cuda_engine(f.read())


class HostDeviceMem(object):
    def __init__(self, host_mem, device_mem):
        self.host = host_mem
        self.device = device_mem

    def __str__(self):
        return "Host:\n" + str(self.host) + "\nDevice:\n" + str(self.device)

    def __repr__(self):
        return self.__str__()


import pycuda.autoinit
import pycuda.driver as cuda


class allocator:
    def __init__(self, engine):
        self.engine = engine

    def __enter__(self):
        self.inputs = []
        self.outputs = []
        self.bindings = []
        self.stream = cuda.Stream()
        for binding in self.engine:
            size = (
                trt.volume(self.engine.get_binding_shape(binding))
                * self.engine.max_batch_size
            )
            dtype = trt.nptype(self.engine.get_binding_dtype(binding))
            # Allocate host and device buffers
            host_mem = cuda.pagelocked_empty(size, dtype)
            device_mem = cuda.mem_alloc(host_mem.nbytes)
            # Append the device buffer to device bindings.
            self.bindings.append(int(device_mem))
            # Append to the appropriate list.
            if self.engine.binding_is_input(binding):
                self.inputs.append(HostDeviceMem(host_mem, device_mem))
            else:
                self.outputs.append(HostDeviceMem(host_mem, device_mem))

        return self.inputs, self.outputs, self.bindings, self.stream

    def __exit__(self, exc_type, exc_val, exc_tb):
        del self.inputs, self.outputs, self.bindings, self.stream


def do_inference(context, bindings, inputs, outputs, stream):
    # Transfer input data to the GPU.
    [cuda.memcpy_htod_async(inp.device, inp.host, stream) for inp in inputs]
    # Run inference.
    context.execute_async_v2(bindings=bindings, stream_handle=stream.handle)
    # Transfer predictions back from the GPU.
    [cuda.memcpy_dtoh_async(out.host, out.device, stream) for out in outputs]
    # Synchronize the stream
    stream.synchronize()
    # Return only the host outputs.
    return [out.host for out in outputs]


from abottle.base_model import BaseModel


class TensorRTModel(BaseModel):
    class Config:
        trt_file = ""

    def __init__(self):
        self.engine = get_engine(self.Config.trt_file)
        self.context = self.engine.create_execution_context()

    def __del__(self):
        del self.context, self.engine

    def infer(self, X={}, Y=[]):

        with allocator(self.engine) as (inputs, outputs, bindings, stream):
            for i, (k, v) in enumerate(X.items()):
                inputs[i].host = v

            return do_inference(
                self.context,
                bindings=bindings,
                inputs=inputs,
                outputs=outputs,
                stream=stream,
            )
