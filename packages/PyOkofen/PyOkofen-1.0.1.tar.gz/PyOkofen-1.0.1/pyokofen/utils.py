def temperature_format(value):
    return round(int(value) * 0.1, 1)


class OkofenDefinition:
    def __init__(self, name=None):
        self.domain = name
        self.__datas = {}

    def set(self, target, value):
        self.__datas[target] = value

    def get(self, target):
        if target in self.__datas:
            return self.__datas[target]
        return None


class OkofenDefinitionHelperMixin:
    def get(self, target):
        return super().get(target)
