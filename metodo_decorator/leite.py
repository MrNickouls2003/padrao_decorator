# leite.py
from decorator import DecoradorBebida

class Leite(DecoradorBebida):
    def custo(self):
        return self.bebida.custo() + 1.5  

    def descricao(self):
        return self.bebida.descricao() + ", Leite"
