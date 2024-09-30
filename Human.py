from Brain import Brain
from Cloth import Cloth
from Heart import Heart
from Organ import Organ


class Human:
    __organs: [Organ]
    __clothes: [Cloth]

    def __init__(self):
        self.__organs = []
        self.__organs.append(Heart())
        self.__organs.append(Brain())
        self.__clothes = []

    def wear(self, cloth: Cloth) -> None:
        self.__clothes.append(cloth)

    def takeOff(self, cloth: Cloth) -> None:
        self.__clothes.remove(cloth)

    def __str__(self):
        result = ""

        for organ in self.__organs:
            result += str(organ) + " "

        result += "\n"

        for cloth in self.__clothes:
            result += str(cloth) + " "

        return result

    def harvest(self, organName: str) -> Organ | None:
        for organ in self.__organs:
            if organName == organ.Name:
                self.__organs.remove(organ)
                return organ
        return None

    def transplant(self, organ: Organ) -> None:
        self.__organs.append(organ)
