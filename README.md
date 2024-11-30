# Descrição
Este é um programa simples em Python para gerenciar uma lista de tarefas. Ele permite adicionar, visualizar, atualizar, marcar como completas e deletar tarefas. O código utiliza um menu interativo para facilitar o uso.

# Funcionalidades
- Adicionar Tarefa
Adiciona uma nova tarefa à lista.

- Ver Tarefas
Exibe todas as tarefas cadastradas, indicando se estão concluídas.

- Atualizar Tarefa
Permite alterar o nome de uma tarefa específica.

- Completar Tarefa
Marca uma tarefa como concluída.

- Deletar Tarefas Completadas
Remove todas as tarefas que já foram concluídas.

Sair
Finaliza o programa.

1. Como Usar

Execute o programa: Certifique-se de que você tem o Python 

instalado e execute o script em um terminal:

         python gerenciador_tarefas.py

2. Navegue pelo menu:

Escolha uma das opções exibidas no menu digitando o número correspondente.

3. Interaja com o programa:

    .Adicionar Tarefa: Insira o nome da tarefa.
    .Ver Tarefas: Visualize todas as tarefas e seus status.
    .Atualizar Tarefa: Escolha o número da tarefa e insira o novo nome.
    .Completar Tarefa: Escolha o número da tarefa para marcá-la como concluída.
    .Deletar Tarefas Completadas: Remova todas as tarefas marcadas como concluídas.
    .Sair: Encerre o programa.


# Estrutura do Código
    .Funções:

        .adicionar_tarefa: Adiciona uma nova tarefa à lista.
        .ver_tarefas: Exibe a lista de tarefas.
        .atualizar_nome_tarefas: Atualiza o nome de uma tarefa.
        .completar_tarefa: Marca uma tarefa como concluída.
        .deletar_tarefas_completadas: Remove todas as tarefas concluídas.

# Estrutura de Dados:

    .Cada tarefa é representada por um dicionário com as chaves:
        ."tarefa": Nome da tarefa.
     ."completada": Status (True para concluída, False para pendente).