import unittest
import calculadora as calc


class TestCalculadora(unittest.TestCase):
    def test_soma_10_10_retorna_20(self):
        self.assertEqual(
            calc.soma(10, 10), 20,
            'concluido com sucesso'
        )


unittest.main(verbosity=2)
