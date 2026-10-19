# Projeto Inicial

história 1 - Reservar atendimento de monitoria.

## classes e sua função

- **Materia:** representa uma disciplina. Guarda o nome. É a chave para filtrar horários.
- **Aluno:** representa quem reserva. Guarda RA e nome. Não faz lógica de reservar.
- **Monitor:** representa quem atende. Guarda RA, nome e a disciplina que atende, responsavel pelos horários que oferece.
- **Horario:** representa o atendimento de 30 minutos. Guarda monitor, disciplina, data/hora de início, capacidade (1 = individual, maior que 1 = grupo) e a lista de reservas ativas. Sabe informar se está livre e quantas vagas restam.
- **Reserva:** representa a ligação entre um aluno e um horário. Guarda aluno, sala, horário e situação (ativa, cancelada, falta, realizada). Nesta história só é criada como "ativa".
- **ServicoReserva:** concentra as regras da história. Mantém a lista de horários e reservas, e oferece:
  - listar os horários livres de uma disciplina;
  - reservar um horário para um aluno, validando existência, capacidade e limite semanal;
  <!-- - consultar o limite semanal (padrão 2 por disciplina, configurável). -->
- **Erros próprios:** HorarioInexistenteError, HorarioLotadoError e !!LimiteSemanalError!!.

## criterios e testes

| critério | teste | resultado |
|---|---|---|
| Lista só horários livres da disciplina | `test_lista_apenas_horarios_livres_da_disciplina` | sucesso |
| Disciplina sem horários livres | `test_lista_vazia_quando_nao_ha_horarios_livres` | falha/limite |
| Reserva registrada e vaga ocupada | `test_reserva_registra_e_ocupa_vaga` | sucesso |
| Horário lotado é recusado | `test_reserva_em_horario_lotado_lanca_erro` | falha |
| Horário em grupo aceita até a capacidade | `test_horario_em_grupo_aceita_ate_a_capacidade` | sucesso |
| Limite semanal excedido é recusado | `test_limite_semanal_excedido_lanca_erro` | falha |
| Semana seguinte não conta no limite | `test_reserva_em_outra_semana_nao_conta_no_limite` | sucesso |
| Horário inexistente é recusado | `test_reserva_em_horario_inexistente_lanca_erro` | falha |

## Registro de mudanças
