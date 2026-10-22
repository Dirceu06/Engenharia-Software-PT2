"""
testes pros horarios do sistema de reservas
"""

import unittest
import sys
from datetime import timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from Horario import Horario
from Reserva import Reserva
from testes.helpers import (
    CALCULO, SEGUNDA, SEGUNDA_SEGUINTE, novo_aluno, novo_monitor,
)

class TestHorario(unittest.TestCase):
    def setUp(self):
        self.monitor = novo_monitor(CALCULO)

    def _horario(self, capacidade=1, inicio=SEGUNDA):
        return Horario(self.monitor, CALCULO, inicio, capacidade)

    def test_fim_e_30_minutos_depois_do_inicio(self):
        self.assertEqual(self._horario().fim, SEGUNDA + timedelta(minutes=30))

    def test_capacidade_invalida_lanca_erro(self):
        with self.assertRaises(ValueError):
            self._horario(capacidade=0)

    def test_horario_novo_esta_livre_com_todas_as_vagas(self):
        horario = self._horario(capacidade=3)
        self.assertTrue(horario.esta_livre())
        self.assertEqual(horario.vagas_restantes(), 3)

    def test_horario_cheio_nao_esta_livre(self):
        horario = self._horario()
        horario.reservas.append(Reserva(novo_aluno(1), horario))
        self.assertFalse(horario.esta_livre())

    def test_reserva_cancelada_libera_vaga(self):
        horario = self._horario()
        reserva = Reserva(novo_aluno(1), horario)
        horario.reservas.append(reserva)
        reserva.situacao = Reserva.CANCELADA
        self.assertTrue(horario.esta_livre())

    def test_semana_difere_entre_semanas(self):
        self.assertNotEqual(
            self._horario().semana, self._horario(inicio=SEGUNDA_SEGUINTE).semana
        )


if __name__ == "__main__":
    unittest.main()
