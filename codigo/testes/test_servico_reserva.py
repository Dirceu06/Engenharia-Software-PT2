"""
testes do módulo serviço de reserva
"""

import unittest
import sys
from datetime import timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from Erros import (
    HorarioInexistenteError,
    HorarioLotadoError,
    LimiteSemanalError,
    ReservaDuplicadaError,
)
from Horario import Horario
from Reserva import Reserva
from Servico_reserva import ServicoReserva
from testes.helpers import (
    CALCULO, FISICA, SEGUNDA, SEGUNDA_SEGUINTE, TERCA, novo_aluno, novo_monitor,
)


class TestReservarAtendimento(unittest.TestCase):
    """testes de aceitação da historia 1"""

    def setUp(self):
        self.servico = ServicoReserva(limite_semanal=2)
        self.monitor = novo_monitor(CALCULO)
        self.aluno = novo_aluno(100)

    def _adicionar(self, inicio, materia=CALCULO, capacidade=1):
        return self.servico.adicionar_horario(
            Horario(self.monitor, materia, inicio, capacidade)
        )

    # criterio 1
    def test_lista_apenas_horarios_livres_da_disciplina(self):
        livre = self._adicionar(SEGUNDA)
        ocupado = self._adicionar(SEGUNDA + timedelta(hours=1))
        self._adicionar(SEGUNDA, materia=FISICA)
        self.servico.reservar(novo_aluno(200), ocupado)

        ids = [h.id for h in self.servico.listar_horarios_livres(CALCULO)]

        self.assertEqual(ids, [livre])

    def test_lista_vazia_quando_nao_ha_horarios_livres(self):
        self._adicionar(SEGUNDA, materia=FISICA)
        self.assertEqual(self.servico.listar_horarios_livres(CALCULO), [])

    # criterio 2
    def test_reserva_registra_e_ocupa_vaga(self):
        horario_id = self._adicionar(SEGUNDA, capacidade=2)

        reserva = self.servico.reservar(self.aluno, horario_id)

        self.assertIsInstance(reserva, Reserva)
        self.assertEqual(reserva.situacao, Reserva.ATIVA)
        self.assertIn(reserva, self.servico.reservas_do_aluno(self.aluno))
        self.assertEqual(reserva.horario.vagas_restantes(), 1)

    # criterio 3
    def test_reserva_em_horario_lotado_lanca_erro(self):
        horario_id = self._adicionar(SEGUNDA)
        self.servico.reservar(novo_aluno(200), horario_id)

        with self.assertRaises(HorarioLotadoError):
            self.servico.reservar(self.aluno, horario_id)

    def test_horario_em_grupo_aceita_ate_a_capacidade(self):
        horario_id = self._adicionar(SEGUNDA, capacidade=3)

        for ra in (1, 2, 3):
            self.servico.reservar(novo_aluno(ra), horario_id)

        self.assertEqual(self.servico.listar_horarios_livres(CALCULO), [])
        with self.assertRaises(HorarioLotadoError):
            self.servico.reservar(novo_aluno(4), horario_id)

    # criterio 4
    def test_limite_semanal_excedido_lanca_erro(self):
        h1 = self._adicionar(SEGUNDA)
        h2 = self._adicionar(TERCA)
        h3 = self._adicionar(TERCA + timedelta(hours=1))
        self.servico.reservar(self.aluno, h1)
        self.servico.reservar(self.aluno, h2)

        with self.assertRaises(LimiteSemanalError):
            self.servico.reservar(self.aluno, h3)

    def test_reserva_em_outra_semana_nao_conta_no_limite(self):
        h1 = self._adicionar(SEGUNDA)
        h2 = self._adicionar(TERCA)
        proxima = self._adicionar(SEGUNDA_SEGUINTE)
        self.servico.reservar(self.aluno, h1)
        self.servico.reservar(self.aluno, h2)

        reserva = self.servico.reservar(self.aluno, proxima)

        self.assertEqual(reserva.situacao, Reserva.ATIVA)

    def test_limite_semanal_e_por_disciplina(self):
        h1 = self._adicionar(SEGUNDA)
        h2 = self._adicionar(TERCA)
        fisica = self._adicionar(SEGUNDA, materia=FISICA)
        self.servico.reservar(self.aluno, h1)
        self.servico.reservar(self.aluno, h2)

        reserva = self.servico.reservar(self.aluno, fisica)

        self.assertEqual(reserva.situacao, Reserva.ATIVA)

    # criterio 5
    def test_reserva_em_horario_inexistente_lanca_erro(self):
        with self.assertRaises(HorarioInexistenteError):
            self.servico.reservar(self.aluno, 999)

    # acrescimo ao projeto inicial
    def test_reserva_duplicada_lanca_erro(self):
        horario_id = self._adicionar(SEGUNDA, capacidade=2)
        self.servico.reservar(self.aluno, horario_id)

        with self.assertRaises(ReservaDuplicadaError):
            self.servico.reservar(self.aluno, horario_id)

    def test_limite_semanal_invalido_lanca_erro(self):
        with self.assertRaises(ValueError):
            ServicoReserva(limite_semanal=0)


if __name__ == "__main__":
    unittest.main()
