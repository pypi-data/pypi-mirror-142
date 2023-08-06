import json
import typing
from json import JSONEncoder
import numpy


class NumpyEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


from fastapi import FastAPI, Request, Body
from fastapi.responses import Response
from pydantic import schema_of
import importlib
import uvicorn
from typing import Any

app = FastAPI()

USERMODEL = None


@app.post("/predict")
async def predict(request: Request, X: typing.Any = Body(...)):
    user_request = await request.json()
    # FIXME: should comprese resposne content
    user_response = USERMODEL.predict(**user_request)
    response_content = json.dumps(user_response, cls=NumpyEncoder)
    # log here
    return Response(content=response_content, media_type="application/json")


@app.post("/metrics")
async def metrics():
    raise NotImplementedError()


@app.get("/healthz")
async def healthz():
    if hasattr(USERMODEL, "status"):
        return USERMODEL.status()
    return True


@app.get("/readyz")
async def readyz():
    if hasattr(USERMODEL, "status"):
        return USERMODEL.status()
    return True


@app.get("/meta")
async def meta():
    if hasattr(USERMODEL, "meta"):
        user_meta = USERMODEL.meta()
        if user_meta:
            return user_meta
    user_meta = USERMODEL.predict.__annotations__
    user_meta_dict = {}
    for key in user_meta:
        user_meta_dict[key] = schema_of(user_meta[key], title=key)
    return user_meta_dict


from .pytorch_model import PytorchModel
from .onnx_model import ONNXModel
from .triton_model import TritonModel

# FIXME: Trt can not be loaded without cuda
# from .trt_model import TensorRTModel

from pathlib import Path
import importlib
import argparse
import os
import sys


def locate(usermodel_name):
    package_dir = Path(__name__).resolve().parent
    sys.path.append(str(package_dir))
    usermodel_names = usermodel_name.split(".")
    module = importlib.import_module(usermodel_names[0])
    my_class = None
    for attr in usermodel_names[1:]:
        my_class = getattr(module, attr)
    return my_class


def load(usermodel_name, load_type, *args, **kwargs):

    usermodel = locate(usermodel_name)()

    if load_type == "TritonModel" and hasattr(usermodel.Config, "TritonModel"):
        triton_model = TritonModel().load_from(usermodel)

    elif load_type == "Pytorch" and hasattr(usermodel.Config, "PytorchModel"):
        pytorch_model = PytorchModel().load_from(usermodel)

    elif load_type == "ONNX" and hasattr(usermodel.Config, "ONNXModel"):
        onnx_model = ONNXModel().load_from(usermodel)

    elif load_type == "TensorRT" and hasattr(usermodel.Config, "TensorRTModel"):
        trt_model = TensorRTModel().load_from(usermodel)

    else:
        raise Exception("no model can be imported")
    return usermodel


def start_server(host, port):
    uvicorn.run(app, host=host, port=port)


def run_tester(*args, **kwargs):
    return USERMODEL.evaluate(*args, **kwargs)


def main():
    parser = argparse.ArgumentParser(
        description="Warp you python object with triton model"
    )
    parser.add_argument("usermodel_name", help="your python object moudle")
    parser.add_argument(
        "--load_type",
        help="which model type you want to load? TritonModel? PytorchModel? ONNXModel? TensorRTModel?",
        default="TritonModel",
    )
    parser.add_argument("--use_as", help="server? tester?", default="server")
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", default=8081)
    # FIXME: shuold set file path and batch size as fix argument?
    args = parser.parse_args()

    global USERMODEL
    USERMODEL = load(**vars(args))

    if args.use_as == "server":
        start_server(args.host, args.port)
    if args.use_as == "tester":
        run_tester()


if __name__ == "__main__":
    main()
