def hanoi(n, origen, destino, auxiliar):
    """
    Función recursiva que resuelve el problema de la Torre de Hanoi y muestra la salida en cada movimiento.

    Parámetros:
    - n: número de discos.
    - origen: poste donde se encuentran los discos inicialmente.
    - destino: poste donde se quiere mover los discos.
    - auxiliar: poste auxiliar para realizar los movimientos.

    """
    if n == 1:
        # Si sólo hay un disco, lo mueve de origen a destino.
        print("Mover disco 1 de", origen, "a", destino)
        return
    
    # Mueve n-1 discos de origen a auxiliar, usando destino como poste auxiliar.
    hanoi(n-1, origen, auxiliar, destino)
    
    # Mueve el disco n de origen a destino.
    print("Mover disco", n, "de", origen, "a", destino)
    
    # Mueve n-1 discos de auxiliar a destino, usando origen como poste auxiliar.
    hanoi(n-1, auxiliar, destino, origen)


# Pedimos al usuario el número de discos
n = int(input("Introduce el número de discos: "))

# Llamamos a la función hanoi
hanoi(n, 'A', 'C', 'B')
