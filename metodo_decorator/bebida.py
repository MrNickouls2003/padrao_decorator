from abc import ABC, abstractmethod

class Bebida(ABC):
    @abstractmethod
    def custo(self):
        pass

    @abstractmethod
    def descricao(self):
        pass
