__author__ = 'dante'


def hanoi(numero_discos, inicio=1, fin=3):
    if(numero_discos):
        hanoi(numero_discos-1, inicio, 6-inicio-fin)
        print("Mueve el disco %d de la torre %d a la torre %d" %
             (numero_discos, inicio, fin))
        hanoi(numero_discos-1, 6-inicio-fin, fin)

hanoi(numero_discos=3)