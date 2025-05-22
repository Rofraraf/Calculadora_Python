import unittest
from calculadora import Calculadora
import math

class TestCalculadora(unittest.TestCase):
    """Pruebas unitarias para la clase Calculadora"""
    
    def setUp(self):
        #Este metodo se ejecuta antes de cada test para preparar el objeto calculadora
        self.calc = Calculadora()
        
    def test_sumar(self):
        """Pruebas básicas para la suma con distintos tipos de valores"""
        self.assertEqual(self.calc.sumar(2, 3), 5)
        self.assertEqual(self.calc.sumar(-2, 3), 1)
        self.assertEqual(self.calc.sumar(0, 0), 0)
        
    def test_restar(self):
        """Pruebas básicas para la resta"""
        self.assertEqual(self.calc.restar(5, 3), 2)
        self.assertEqual(self.calc.restar(-2, -3), 1)
        self.assertEqual(self.calc.restar(0, 0), 0)
        
    def test_multiplicar(self):
        """Pruebas básicas para la multiplicación con enteros y cero"""
        self.assertEqual(self.calc.multiplicar(4, 5), 20)
        self.assertEqual(self.calc.multiplicar(-2, 3), -6)
        self.assertEqual(self.calc.multiplicar(0, 10), 0)

    def test_dividir(self): 
        """Pruebas para la división con resultados positivos, negativos y cero""" 
        self.assertEqual(self.calc.dividir(10, 2), 5)
        self.assertEqual(self.calc.dividir(-10, 2), -5)
        self.assertEqual(self.calc.dividir(0, 5), 0)
        
    def test_dividir_por_cero(self):
        """Prueba que comprueba que dividir por cero lanza un ZeroDivisionError"""
        with self.assertRaises(ZeroDivisionError):
            self.calc.dividir(5,0)
            
    def test_division_con_nan(self):
        """Prueba que simula un resultado NaN, usado para representar resultados indefinidos.
                
        Ejemplo práctico:
        - Un promedio de una lista vacía o una operación inválida en estadísticas     
        en algunos lenguajes como JavaScript, podría devolverse NaN. Pero en Python, 0.0 / 0.0 lanza error,
        pero aquí comprobamos explícitamente un NaN para demostrar que lo manejamos."""
        
        resultado = float("nan") #Simulación de un NaN
        self.assertTrue(math.isnan(resultado))
        
    def test_division_con_infinito(self):
        """Prueba que simula una división que da como resultado infinito positivo.
        
        Ejemplo práctico:
        - En ciertas operaciones donde se divide entre un valor muy cercano a cero, el resultado puede crecer tanto
        que se aproxima al infinito. Con este test manejamos el error"""
        
        resultado = self.calc.dividir(1e308, 1e-10)
        self.assertTrue(math.isinf(resultado))
    
    def test_suma_con_none(self):
        """Prueba que verifica que pasar 'None' como uno de los argumentos lanza un TypeError
        
        Ejemplo práctico:
        - Una función espera 2 numeros, pero recibe un valor sin inicializar
        Python debe avisar que no se puede operar con 'None'."""
        
        with self.assertRaises(TypeError):
            self.calc.sumar(None, 5)
            
    def test_division_con_cadena(self):
        """Verificamos que pasar texto como número lanza un TypeError
        
        Ejemplo práctico:
        - Si en una calculadora web el usuario escribe "10" como texto y no se valida,
        puede producir un fallo si se intenta dividirlo"""
        
        with self.assertRaises(TypeError):
            self.calc.dividir("10", 2)
            
    def test_precision_decimal(self):
        """Evalúa si la división entre decimales largos se maneja correctamente.
        
        Ejemplo práctico:
        - A veces se necesitan resultados con alta precisión. Esta prueba compara el resultado
        con una aproximación esperada, aceptando ligeras variaciones.
        """
        
        resultado = self.calc.dividir(1.123456789, 3.000000001)
        self.assertAlmostEqual(resultado, 0.374485595, places=6)
        
if __name__ == '__main__':
    unittest.main()