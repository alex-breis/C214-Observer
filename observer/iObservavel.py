from abc import ABC, abstractmethod

class IObservavel(ABC):

    @abstractmethod
    def registra_observador(self, observador):
        pass

    @abstractmethod
    def remove_observador(self, observador):
        pass

    @abstractmethod
    def notifica_observadores(self):
        pass
