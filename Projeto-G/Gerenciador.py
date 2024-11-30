def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa '{nome_tarefa}' foi adicionada com sucesso!")

def ver_tarefas(tarefas):
    print("\nLista de tarefas:")
    if not tarefas:  # Verifica se a lista está vazia
        print("Nenhuma tarefa cadastrada.")
    else:
        for indice, tarefa in enumerate(tarefas, start=1):
            status = "✓" if tarefa["completada"] else " "
            nome_tarefa = tarefa["tarefa"]
            print(f"{indice}. [{status}] {nome_tarefa}")

while True:
    print("\nMenu do Gerenciador de Lista de tarefas: ")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar Tarefas ")
    print("4. Completar Tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")