"""
módulo com as funções auxiliares pros testes
"""

from datetime import datetime
from types import SimpleNamespace

CALCULO = SimpleNamespace(nome="Cálculo")
FISICA = SimpleNamespace(nome="Física")

# 26/10/2026 é segunda feira
# 02/11/2026 é a segunda da semana seguinte
SEGUNDA = datetime(2026, 10, 26, 14, 0)
TERCA = datetime(2026, 10, 27, 14, 0)
SEGUNDA_SEGUINTE = datetime(2026, 11, 2, 14, 0)

def novo_aluno(ra):
    return SimpleNamespace(ra=ra, nome=f"Aluno {ra}")

def novo_monitor(materia):
    return SimpleNamespace(ra=1, nome="Monitor", materia=materia)
