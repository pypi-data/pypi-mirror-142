import os
import tensorrt as trt

TRT_LOGGER = trt.Logger()


def get_engine(engine_file_path=""):
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


def allocate_buffers(engine):
    inputs = []
    outputs = []
    bindings = []
    stream = cuda.Stream()
    for binding in engine:
        size = trt.volume(engine.get_binding_shape(binding)) * engine.max_batch_size
        dtype = trt.nptype(engine.get_binding_dtype(binding))
        # Allocate host and device buffers
        host_mem = cuda.pagelocked_empty(size, dtype)
        device_mem = cuda.mem_alloc(host_mem.nbytes)
        # Append the device buffer to device bindings.
        bindings.append(int(device_mem))
        # Append to the appropriate list.
        if engine.binding_is_input(binding):
            inputs.append(HostDeviceMem(host_mem, device_mem))
        else:
            outputs.append(HostDeviceMem(host_mem, device_mem))
    return inputs, outputs, bindings, stream


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


class TensorRTModel:
    class Config:
        trt_file = ""

    def __init__(self):
        self.eng = get_engine(self.Config.trt_file)
        self.context = self.eng.create_execution_context()

    def __del__(self):
        del self.context, self.eng

    def load_from(self, usermodel):
        self.Config = usermodel.Config.TensorRTModel
        usermodel.model = self
        return self

    def infer(self, X=[], Y=[]):

        with allocate_buffers(self.eng) as inputs, outputs, bindings, stream:
            for i, x in enumerate(X.items()):
                inputs[i].host = x

            return do_inference(
                self.context,
                bindings=bindings,
                inputs=inputs,
                outputs=outputs,
                stream=stream,
            )
