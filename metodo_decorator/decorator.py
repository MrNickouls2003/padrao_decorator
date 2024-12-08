from bebida import Bebida
from abc import ABC

class DecoradorBebida(Bebida, ABC):
    def __init__(self, bebida):
        self.bebida = bebida

    def custo(self):
        return self.bebida.custo()

    def descricao(self):
        return self.bebida.descricao()
