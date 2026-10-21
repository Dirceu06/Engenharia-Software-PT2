"""
testes pros erros do sistema de reservas
"""

import unittest

from Erros import (
    HorarioInexistenteError,
    HorarioLotadoError,
    LimiteSemanalError,
    ReservaDuplicadaError,
    ReservaError,
)

class TestErros(unittest.TestCase):
    def test_todos_herdam_de_reserva_error(self):
        for erro in (
            HorarioInexistenteError,
            HorarioLotadoError,
            LimiteSemanalError,
            ReservaDuplicadaError,
        ):
            self.assertTrue(issubclass(erro, ReservaError))

    def test_mensagem_e_preservada(self):
        with self.assertRaises(HorarioLotadoError) as contexto:
            raise HorarioLotadoError("sem vagas")
        self.assertEqual(str(contexto.exception), "sem vagas")

if __name__ == "__main__":
    unittest.main()
