from abc import ABC, abstractmethod


class PyATB(ABC):

    @abstractmethod
    def payFee(self):
        pass

    def enrolled(self):
        print("Enrolled")


class Vimal(PyATB):

    def payFee(self):
        print("Paid")


vimal = Vimal()
vimal.enrolled()
