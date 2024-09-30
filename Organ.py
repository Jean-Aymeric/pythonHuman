from abc import ABC


class Organ(ABC):
    __name: str

    def __init__(self, name: str):
        self.__name = name

    @property
    def Name(self) -> str:
        return self.__name

    def __str__(self):
        return self.Name
