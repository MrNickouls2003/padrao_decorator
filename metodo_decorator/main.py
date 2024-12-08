# main.py
from cafe import Cafe
from leite import Leite
from chocolate import Chocolate

def main():
    bebida = Cafe()
    print(f"{bebida.descricao()} custa ${bebida.custo()}")

    # Adicionando leite
    bebida_com_leite = Leite(bebida)
    print(f"{bebida_com_leite.descricao()} custa ${bebida_com_leite.custo()}")

    # Adicionando chocolate
    bebida_com_chocolate = Chocolate(bebida)
    print(f"{bebida_com_chocolate.descricao()} custa ${bebida_com_chocolate.custo()}")

    # Adicionando leite e chocolate
    bebida_com_leite_e_chocolate = Chocolate(bebida_com_leite)
    print(f"{bebida_com_leite_e_chocolate.descricao()} custa ${bebida_com_leite_e_chocolate.custo()}")

if __name__ == "__main__":
    main()
