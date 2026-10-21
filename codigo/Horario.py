from datetime import timedelta

DURACAO = timedelta(minutes=30)

class Horario:
    def __init__(self, monitor, materia, inicio, capacidade=1):
        if capacidade < 1:
            raise ValueError("A capacidade deve ser de pelo menos 1.")
        self.id = None  # definido pelo ServicoReserva na hora de add um horario
        self.monitor = monitor
        self.materia = materia
        self.inicio = inicio
        self.capacidade = capacidade
        self.reservas = []

    @property
    def fim(self):
        return self.inicio + DURACAO

    @property
    def semana(self):
        ano, semana, _ = self.inicio.isocalendar()
        return (ano, semana)

    def vagas_ocupadas(self):
        return sum(1 for r in self.reservas if r.ocupa_vaga())

    def vagas_restantes(self):
        return self.capacidade - self.vagas_ocupadas()

    def esta_livre(self):
        return self.vagas_restantes() > 0