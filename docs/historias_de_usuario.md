<h1 align="center"> Histórias de Usuário <br> Sistema de agendamento de monitorias</h1>

Premissas assumidas (cliente ainda não decidiu):
- Cada atendimento dura 30 minutos.
- Limite de 2 reservas por semana por disciplina, configurável.
- Cada horário tem uma capacidade (1 = individual; maior que 1 = atendimento em grupo), definida pelo monitor.
- Faltas não bloqueiam o aluno automaticamente; só geram aviso após um limite configurável (por padrão: 3).

## história 1: reservar atendimento de monitoria

Como aluno, quero escolher uma disciplina, ver os horários livres e reservar um atendimento de 30 minutos, pra não precisar combinar horário por mensagem com o monitor.

**critérios de aceitação:**
- quando escolher uma disciplina, o sistema lista apenas os horários livres dessa disciplina.
- ao reservar um horário livre, a reserva é registrada e uma vaga do horário é ocupada.
- se o horário já atingiu a capacidade, a reserva é recusada com erro.
- se o aluno já atingiu o limite semanal de reservas na disciplina, a nova reserva é recusada.
- horários reservados não são exibidos como possibilidade de reserva na tabela de horários.

**prioridade:** Alta. É basicamente a principal ideia de implementação vinda do email.

**trecho do e-mail:** "A ideia é que o aluno escolha a disciplina, veja os horários livres e reserve um atendimento."

## história 2: cancelar atendimento e avisar os alunos

Como monitor, quero que ao cancelar um horário de atendimento, os alunos com reserva sejam avisados, para que ninguém chegue na sala e encontre o atendimento cancelado.

**critérios de aceitação:**
- ao cancelar um horário, ele passa para a situação "cancelado" e deixa de aparecer como livre.
- todas as reservas desse horário passam para a situação "cancelada".
- cada aluno com reserva afetada recebe uma notificação registrada, com disciplina, data e hora.
- um monitor só pode cancelar horários da própria disciplina; caso contrário, o cancelamento é recusado.

**prioridade:** Alta. Os alunos só descobrem o cancelamento ao chegar, gerando perda de tempo.

**trecho do e-mail:** "[...] às vezes precisa cancelar por causa de prova. Os alunos reclamam que só descobrem o cancelamento quando chegam na sala."

## história 3: controlar faltas dos alunos

Como monitor, quero registrar quando um aluno reserva e não comparece, para ter o controle das faltas e avisar o aluno e a coordenação quando forem excessivas.

**critérios de aceitação:**
- o monitor só pode registrar falta em reservas da sua disciplina cujo horário já passou.
- a falta registrada guarda aluno, disciplina, horário e, opcionalmente, o motivo.
- a reserva faltada passa para a situação "falta" e o contador de faltas do aluno aumenta em 1.
- quando o contador atinge o limite configurado, são gerados avisos para o aluno e para a coordenação, sem bloquear novas reservas.

**Prioridade:** Média. O horário perdido é um problema, mas o cliente não decidiu a regra de bloqueio e a reserva funcionando já resolve a maior parte.

**Trecho do e-mail:** "Quando o aluno reserva e não aparece, o horário fica perdido. Alguns monitores sugeriram bloquear quem falta muito, mas outros acham isso exagerado."

## história 4: ver os conteúdos que mais geram dúvidas

Como professor, quero consultar os assuntos mais citados nos atendimentos da disciplina, pra reforçar esses conteúdos em aula.

**critérios de aceitação:**
- após um atendimento realizado, o monitor registra o assunto e um resumo das dúvidas.
- o professor visualiza a lista de assuntos da sua disciplina ordenada do mais para o menos frequente.
- o professor não vê dados de disciplinas de outros professores.
- se não existir atendimentos com assunto registrado, o sistema informa que não há dados.

**prioridade:** Baixa. É útil pro ensino, mas não é necessária para o funcionamento das reservas.

**trecho do e-mail:** "Os professores das disciplinas gostariam de saber quais conteúdos geram mais dúvidas, para reforçar em aula."

## história 5: relatório mensal de horas dos monitores

Como coordenador,quero gerar um relatório mensal com as horas atendidas por cada monitor, pra calcular o pagamento das bolsas.

**critérios de aceitação:**
- o relatório lista, para o mês escolhido, as horas atendidas por cada monitor.
- só contam atendimentos realizados; horários cancelados e sem nenhum aluno presente não contam.
- atendimento em grupo conta uma única vez, e não uma vez por aluno.
- apenas o coordenador acessa o relatório; alunos, monitores e professores recebem acesso negado.

**prioridade:** Média. A coordenação precisa dele todo mês, mas depende de existirem atendimentos registrados.

**trecho do e-mail:** "A coordenação precisa de um relatório mensal com as horas atendidas por cada monitor, porque isso conta para o pagamento da bolsa. Essas informações de bolsa não podem ficar visíveis para todo mundo."