def hanoi(n, inicio, final, auxiliar):
    """
    Esta función resuelve el juego de Torres de Hanoi para n discos.

    n: número de discos
    inicio: torre de inicio (1, 2 o 3)
    final: torre final (1, 2 o 3)
    auxiliar: torre auxiliar (1, 2 o 3)
    """
    if n == 1:
        print("Mover disco 1 de la torre", inicio, "a la torre", final)
        return

    hanoi(n-1, inicio, auxiliar, final)
    print("Mover disco", n, "de la torre", inicio, "a la torre", final)
    hanoi(n-1, auxiliar, final, inicio)

# Ejemplo de uso
hanoi(3, 1, 3, 2)