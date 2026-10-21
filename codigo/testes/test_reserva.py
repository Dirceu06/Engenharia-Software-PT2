"""
teste do módulo reserva
"""

import unittest

from Horario import Horario
from Reserva import Reserva
from testes.helpers import CALCULO, SEGUNDA, novo_aluno, novo_monitor


class TestReserva(unittest.TestCase):
    def setUp(self):
        horario = Horario(novo_monitor(CALCULO), CALCULO, SEGUNDA)
        self.reserva = Reserva(novo_aluno(1), horario)

    def test_reserva_nova_comeca_ativa(self):
        self.assertEqual(self.reserva.situacao, Reserva.ATIVA)
        self.assertTrue(self.reserva.ocupa_vaga())

    def test_reserva_cancelada_nao_ocupa_vaga(self):
        self.reserva.situacao = Reserva.CANCELADA
        self.assertFalse(self.reserva.ocupa_vaga())

    def test_falta_e_realizada_continuam_ocupando_vaga(self):
        for situacao in (Reserva.FALTA, Reserva.REALIZADA):
            self.reserva.situacao = situacao
            self.assertTrue(self.reserva.ocupa_vaga())


if __name__ == "__main__":
    unittest.main()
