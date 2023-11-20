from abc import ABC, abstractmethod

class IObservador(ABC):

    @abstractmethod
    def update(self,observavel):
        pass