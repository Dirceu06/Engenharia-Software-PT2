# 3. Relatório de Execução

Sistema de reserva de monitorias (Atividade Avaliativa A2). Implementa a **História 1: Reservar atendimento de monitoria**. Integrantes: Lucas Henrique Motta (RA 2669730) e Dirceu Morais da Costa Júnior (RA 2669455).

## Como executar
- **Python:** 3.8 ou superior (testado com 3.15 e 3.14.7).
- **Bibliotecas:** nenhuma além da biblioteca padrão.
- **Arquivo principal:** `codigo/main.py`. Comando: `python codigo/main.py`
- **Testes** (na raiz do repositório): `python -m unittest discover -s codigo -v`

## Plano x realizado

| Etapa do plano | Data planejada | Realizado (responsável) |
|---|---|---|
| Histórias de usuário e projeto inicial | Dia 1 (19/10) | Dirceu: Projeto inicial, Lucas: histórias do usuário|
| Implementação das classes | Dias 2-3 (20-21/10) | Dirceu: Monitor, aluno e Materia, Lucas: Erros, Reserva, Serviço_reserva e Horário |
| Testes automatizados | Dias 2-3 (20-21/10) | Lucas |
| Documentação | Dia 4 (22/10) | Dirceu |

## Mudanças em relação ao plano e ao projeto inicial

1. **UML substituído por projeto textual.** O plano da Parte 1 previa UML, mas o enunciado exige projeto inicial sem diagramas.
2. **Classes acrescentadas:** `Horario`, `ServicoReserva` e `erros.py` (exceções próprias). As regras de capacidade e de limite semanal precisavam de um lugar que os testes chamassem direto, sem entrada digitada.
3. **Fora do escopo:** `Professor`, `Falta`, senha e login. A História 1 não os usa; as histórias 2 a 5 foram apenas especificadas.
4. **`ReservaDuplicadaError` acrescentado.** Sem ele, o mesmo aluno poderia ocupar duas vagas de um mesmo horário em grupo.
5. **Testes além da tabela do projeto inicial:** limite semanal por disciplina, limite inválido, reserva duplicada e testes de unidade de `Horario`, `Reserva` e erros.
6. **Premissas** (cliente não decidiu): limite de 2 reservas por semana por disciplina, configurável; capacidade do horário definida pelo monitor.