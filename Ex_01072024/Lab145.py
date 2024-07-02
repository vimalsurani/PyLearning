from abc import ABC, abstractmethod


class ATB(ABC):

    def enorlled(self):
        print("Enrolled")

    @abstractmethod
    def perform_task1(self):
        pass

    @abstractmethod
    def perform_task2(self):
        pass


class Vimal(ATB):
    def perform_task1(self):
        return "Done Task 1"

    def perform_task2(self):
        return "Done Task 2"


vimal = Vimal()
print(vimal.perform_task2())
print(vimal.perform_task1())
