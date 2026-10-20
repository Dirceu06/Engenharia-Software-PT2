# classe Monitor
class Monitor:
    def __init__(self, ra, nome, materia):
        self.ra = ra
        self.nome = nome
        self.materia = materia

    def __str__(self):
        return f"{self.nome} ({self.ra}) - {self.materia}"