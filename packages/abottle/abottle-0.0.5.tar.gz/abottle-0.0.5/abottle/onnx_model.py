import onnxruntime as ort


class ONNXModel:
    class Config:
        ort_file = ""

    def __init__(self):
        self.session = ort.InferenceSession(
            self.Config.ort_file,
            providers=["CUDAExecutionProvider"],
        )

    def infer(self, X={}, Y=[]):
        return self.session.run(None, X)

    def load_from(self, usermodel):
        self.Config = usermodel.Config.ONNXModel
        usermodel.model = self
        return self
