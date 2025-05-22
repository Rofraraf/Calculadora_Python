class Calculadora:
    """Clase que implementa operaciones matemáticas básicas."""

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Error: Intento de división entre cero.")
        return a / b