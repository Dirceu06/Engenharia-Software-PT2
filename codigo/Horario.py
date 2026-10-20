from datetime import timedelta

DURACAO = timedelta(minutes=30)

class Horario:
    def __init__(self, monitor, materia, inicio, capacidade=1):
        if capacidade < 1:
            raise ValueError("A capacidade deve ser de pelo menos 1.")
        self.id = None  # definido pelo ServicoReserva ao adicionar o horário
        self.monitor = monitor
        self.materia = materia
        self.inicio = inicio
        self.capacidade = capacidade
        self.reservas = []
        ano, semana, _ = self.inicio.isocalendar()
        self.semana = (ano, semana)

    def vagas_ocupadas(self):
        return sum(1 for r in self.reservas if r.ocupa_vaga())

    def vagas_restantes(self):
        return self.capacidade - self.vagas_ocupadas()

    def esta_livre(self):
        return self.vagas_restantes() > 0

    def fim(self):
        return self.inicio + DURACAO

    def semana(self):
        ano, semana, _ = self.inicio.isocalendar()
        return (ano, semana)
