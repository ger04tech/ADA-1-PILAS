class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()

    def __str__(self):
        return str(self.items)

def mover_disco(origen, destino):
    disco = origen.desapilar()
    destino.apilar(disco)
    print(f"Se movió el disco {disco} de {origen} a {destino}")

def resolver_hanoi(n, origen, auxiliar, destino):
    if n == 1:
        mover_disco(origen, destino)
    else:
        resolver_hanoi(n - 1, origen, destino, auxiliar)
        mover_disco(origen, destino)
        resolver_hanoi(n - 1, auxiliar, origen, destino)
origen = Pila()
auxiliar = Pila()
destino = Pila()

origen.apilar(2)
origen.apilar(1)

resolver_hanoi(2, origen, auxiliar, destino)
