__author__ = 'dante'


def hanoi(numero_discos: int, inicio=1, fin=3) -> None:
    if(numero_discos):
        hanoi(numero_discos-1, inicio, 6-inicio-fin)
        print(f"Mueve el disco {numero_discos} de la torre {inicio} a la torre {fin}")
        hanoi(numero_discos-1, 6-inicio-fin, fin)

hanoi(numero_discos=6)
