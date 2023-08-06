class PytorchModel:
    class Config:
        model = None

    def infer(self, X={}, Y=[]):
        return model(**X)

    def load_from(self, usermodel):
        self.Config = usermodel.Config.PytorchModel
        usermodel.model = self
        return self
