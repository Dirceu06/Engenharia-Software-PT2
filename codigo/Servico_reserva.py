from Erros import (
    HorarioInexistenteError,
    HorarioLotadoError,
    LimiteSemanalError,
    ReservaDuplicadaError,
)
from Reserva import Reserva


class ServicoReserva:
    def __init__(self, limite_semanal=2):
        if limite_semanal < 1:
            raise ValueError("O limite semanal deve ser de pelo menos 1.")
        self.limite_semanal = limite_semanal
        self._horarios = {}
        self._reservas = []
        self._proximo_id = 1

    def adicionar_horario(self, horario):
        horario.id = self._proximo_id
        self._horarios[horario.id] = horario
        self._proximo_id += 1
        return horario.id

    def listar_horarios_livres(self, materia):
        livres = [
            h for h in self._horarios.values()
            if h.materia.nome == materia.nome and h.esta_livre()
        ]
        return sorted(livres, key=lambda h: h.inicio)

    def reservar(self, aluno, horario_id):
        horario = self._horarios.get(horario_id)
        if horario is None:
            raise HorarioInexistenteError(f"Não existe horário com id {horario_id}.")
        if self._aluno_ja_reservou(aluno, horario):
            raise ReservaDuplicadaError("O aluno já tem reserva neste horário.")
        if not horario.esta_livre():
            raise HorarioLotadoError("Este horário não tem mais vagas.")
        if self._reservas_na_semana(aluno, horario) >= self.limite_semanal:
            raise LimiteSemanalError(
                f"Limite de {self.limite_semanal} reservas por semana "
                f"em {horario.materia.nome} atingido."
            )
        reserva = Reserva(aluno, horario)
        horario.reservas.append(reserva)
        self._reservas.append(reserva)
        return reserva

    def reservas_do_aluno(self, aluno):
        return [r for r in self._reservas if r.aluno.ra == aluno.ra]

    def _aluno_ja_reservou(self, aluno, horario):
        return any(
            r.horario is horario and r.ocupa_vaga()
            for r in self.reservas_do_aluno(aluno)
        )

    def _reservas_na_semana(self, aluno, horario):
        return sum(
            1 for r in self.reservas_do_aluno(aluno)
            if r.ocupa_vaga()
            and r.horario.materia.nome == horario.materia.nome
            and r.horario.semana() == horario.semana()
        )
