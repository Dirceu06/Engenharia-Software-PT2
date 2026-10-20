"""
Dirceu Morais da Costa Júnior (2669455)
Lucas Henrique Motta          (2669730)

Parte 2 - Engenharia de Software
Este arquivo apenas roda todo o programa como demonstração, sem interface gráfica.
"""

from datetime import datetime, timedelta

from Aluno import Aluno
from Erros import ReservaError
from Horario import Horario
from Materia import Materia
from Monitor import Monitor
from Servico_reserva import ServicoReserva

def criar_materia(nome):
    return Materia(nome)


def criar_monitor(ra, nome, materia):
    return Monitor(ra, nome, materia)


def criar_aluno(ra, nome):
    return Aluno(ra, nome)


def montar_dados_iniciais():
    """Cria materias, monitores e horários de exemplo para a demonstração."""
    servico = ServicoReserva(limite_semanal=2)
    materias = [criar_materia(n) for n in ("Cálculo", "Física", "POO", "Estruturas de Dados")]
    amanha = (datetime.now() + timedelta(days=1)).replace(hour=14, minute=0, second=0, microsecond=0)
    for i, materia in enumerate(materias):
        monitor = criar_monitor(1000 + i, f"Monitor de {materia.nome}", materia)
        for dia in range(3):
            for hora in (0, 1):
                inicio = amanha + timedelta(days=dia, hours=hora)
                capacidade = 3 if hora == 1 else 1  # 2o horario do dia é em grupo
                servico.adicionar_horario(Horario(monitor, materia, inicio, capacidade))
    return servico, materias


def formatar_horario(horario):
    return (
        f"[{horario.id}] {horario.inicio:%d/%m %H:%M}-{horario.fim():%H:%M} "
        f"| {horario.monitor.nome} | vagas: {horario.vagas_restantes()}/{horario.capacidade}"
    )


def escolher_materia(materias):
    for i, materia in enumerate(materias, start=1):
        print(f"  {i}. {materia.nome}")
    try:
        return materias[int(input("Disciplina: ")) - 1]
    except (ValueError, IndexError):
        print("Opção inválida.")
        return None


def listar(servico, materias):
    materia = escolher_materia(materias)
    if materia is None:
        return
    horarios = servico.listar_horarios_livres(materia)
    if not horarios:
        print("Nenhum horário livre para esta disciplina.")
    for horario in horarios:
        print(formatar_horario(horario))


def reservar(servico, aluno):
    try:
        horario_id = int(input("Número do horário: "))
        reserva = servico.reservar(aluno, horario_id)
        print(f"Reserva confirmada: {formatar_horario(reserva.horario)}")
    except ValueError:
        print("Digite um número válido.")
    except ReservaError as erro:
        print(f"Não foi possível reservar: {erro}")


def minhas_reservas(servico, aluno):
    reservas = servico.reservas_do_aluno(aluno)
    if not reservas:
        print("Você não tem reservas.")
    for r in reservas:
        print(f"{r.horario.materia.nome} - {formatar_horario(r.horario)} ({r.situacao})")


def main():
    servico, materias = montar_dados_iniciais()
    print("Reserva de Monitorias")
    aluno = criar_aluno(input("Seu RA: ").strip(), input("Seu nome: ").strip())
    while True:
        print("\n1. Ver horários livres  2. Reservar  3. Minhas reservas  0. Sair")
        opcao = input("> ").strip()
        if opcao == "1":
            listar(servico, materias)
        elif opcao == "2":
            reservar(servico, aluno)
        elif opcao == "3":
            minhas_reservas(servico, aluno)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()