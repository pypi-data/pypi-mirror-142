class BaseModel:
    class Config:
        """you can set any field you like in your config class"""

        pass

    def infer(self, X={}, Y=[]):
        """infer function you can do anything here"""
        raise NotImplementedError()

    def evaluate(self, *args, **kwargs):
        raise NotImplementedError()

    def load_from(self, usermodel):
        """you shuold set your wrapper from usermodel, and set Config like"""
        self.Config = getattr(usermodel.Config, self.__class__.__name__)
        usermodel.model = self
        return usermodel
