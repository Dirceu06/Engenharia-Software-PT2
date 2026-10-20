# classe Aluno
class Aluno:
    def __init__(self, ra, nome):
        self.ra = ra
        self.nome = nome

    def __str__(self):
        return f"{self.nome} ({self.ra})"
    