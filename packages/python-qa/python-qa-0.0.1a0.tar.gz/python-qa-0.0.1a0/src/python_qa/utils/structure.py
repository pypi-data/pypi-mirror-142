class StructDict:
    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)
        for key, value in self.__dict__.items():
            if isinstance(value, dict):
                self.__dict__[key] = StructDict(**value)
