class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

def evaluar_postfija(expresion):
    pila = Pila()  
    for char in expresion:
        if char.isdigit():  
            pila.apilar(int(char))
        else:  
            num2 = pila.desapilar()
            num1 = pila.desapilar()
            if char == '+':
                pila.apilar(num1 + num2)
    return pila.desapilar()

expresion_postfija = "23+"
resultado = evaluar_postfija(expresion_postfija)
print(f"El resultado de la expresión {expresion_postfija} es: {resultado}")
