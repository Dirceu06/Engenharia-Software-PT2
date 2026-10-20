class Reserva:
    ATIVA = "ativa"
    CANCELADA = "cancelada"
    FALTA = "falta"
    REALIZADA = "realizada"

    def __init__(self, aluno, horario):
        self.aluno = aluno
        self.horario = horario
        self.situacao = Reserva.ATIVA

    def ocupa_vaga(self):
        # só a reserva cancelada libera a vaga e deixa de contar no limite
        return self.situacao != Reserva.CANCELADA
