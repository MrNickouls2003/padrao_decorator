# chocolate.py
from decorator import DecoradorBebida

class Chocolate(DecoradorBebida):
    def custo(self):
        return self.bebida.custo() + 2.0  

    def descricao(self):
        return self.bebida.descricao() + ", Chocolate"
