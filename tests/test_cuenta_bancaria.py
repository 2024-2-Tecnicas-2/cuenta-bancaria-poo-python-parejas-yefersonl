import sys
import os
import unittest

# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from cuenta_bancaria import CuentaBancaria

class CuentaBancariaTest(unittest.Testdef):

    def setUp(self):
        # Método que se llama antes de cada prueba, para inicializar datos comunes
        self.cuenta = CuentaBancaria("Jorge", "12345", 1000, 0.015)

    def testGetTitular(self):
        valor_esperado = "Jorge"
        self.cuenta.setTitular("Jorge")
        valor_actual = self.cuenta.getTitular()
        self.assertEqual(valor_esperado, valor_actual)

    def testGetTitular2(self):
        valor_esperado = "Leonardo"
        self.cuenta.setTitular("Leonardo")
        valor_actual = self.cuenta.getTitular()
        self.assertEqual(valor_esperado, valor_actual)

    def testGetNumeroCuenta(self):
        valor_esperado = "12345"
        self.cuenta.setNumeroCuenta("12345")
        valor_actual = self.cuenta.getNumeroCuenta()
        self.assertEqual(valor_esperado, valor_actual)

    def testGetNumeroCuenta2(self):
        valor_esperado = "506232710L"
        self.cuenta.setNumeroCuenta("506232710L")
        valor_actual = self.cuenta.getNumeroCuenta()
        self.assertEqual(valor_esperado, valor_actual)

    def testGetSaldo(self):
        valor_esperado = 1000
        self.cuenta.setSaldo(1000)
        valor_actual = self.cuenta.getSaldo()
        self.assertEqual(valor_esperado, valor_actual)

    def testGetSaldo2(self):
        valor_esperado = 500
        self.cuenta.setSaldo(500)
        valor_actual = self.cuenta.getSaldo()
        self.assertEqual(valor_esperado, valor_actual)

    def testIngresar(self):
        self.cuenta.ingresar(500)
        valor_esperado = 1500
        valor_actual = self.cuenta.getSaldo()
        self.assertEqual(valor_esperado, valor_actual)

    def testRetirar(self):
        self.cuenta.retirar(500)
        valor_esperado = 500
        valor_actual = self.cuenta.getSaldo()
        self.assertEqual(valor_esperado, valor_actual)

    def testRetirarInsuficiente(self):
        self.cuenta.retirar(2000)
        valor_esperado = 1000
        valor_actual = self.cuenta.getSaldo()
        self.assertEqual(valor_esperado, valor_actual)

    def testCalcularInteres(self):
        valor_esperado = 1000 * 0.015
        valor_actual = self.cuenta.calcularInteres()
        self.assertEqual(valor_esperado, valor_actual)

    def testCalcularInteresNegativo(self):
        self.cuenta.setSaldo(-1000)
        valor_actual = self.cuenta.calcularInteres()
        self.assertEqual(0, valor_actual)

    def testSetTipoInteres(self):
        self.cuenta.setTipoInteres(0.10)
        valor_esperado = 0.10
        valor_actual = self.cuenta.getTipoInteres()
        self.assertEqual(valor_esperado, valor_actual)

    def testSetTipoInteresInvalido(self):
        self.cuenta.setTipoInteres(-0.10)
        valor_esperado = 0.015
        valor_actual = self.cuenta.getTipoInteres()
        self.assertEqual(valor_esperado, valor_actual)

if __name__ == '__main__':
    unittest.main()
