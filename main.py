import sqlite3
import os
from tabulate import tabulate
from colorama import init, Fore, Style

# Inicializar a Colorama para Windows (opcional em outros sistemas)
init(autoreset=True)

# Conexão com o banco de dados SQLite
def connect_db():
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tarefas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        description TEXT NOT NULL,
                        completed INTEGER NOT NULL DEFAULT 0)''')
    conn.commit()
    return conn, cursor

# Função para limpar a tela
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para adicionar nova tarefa
def add_task(description):
    conn, cursor = connect_db()
    cursor.execute("INSERT INTO tarefas (description) VALUES (?)", (description,))
    conn.commit()
    conn.close()
    print(Fore.GREEN + "Tarefa adicionada com sucesso!")

# Função para visualizar todas as tarefas
def view_tarefas():
    conn, cursor = connect_db()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    conn.close()

    if tarefas:
        table = [[task[0], task[1], Fore.GREEN + 'Concluída' if task[2] else Fore.RED + 'Pendente'] for task in tarefas]
        print(Fore.CYAN + "\nLista de Tarefas:")
        print(tabulate(table, headers=['ID', 'Descrição', 'Status'], tablefmt='grid'))
    else:
        print(Fore.YELLOW + "\nNenhuma tarefa cadastrada!")

# Função para marcar uma tarefa como concluída
def complete_task(task_id):
    conn, cursor = connect_db()
    cursor.execute("UPDATE tarefas SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    print(Fore.GREEN + "Tarefa marcada como concluída!")

# Função para remover uma tarefa
def remove_task(task_id):
    conn, cursor = connect_db()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    print(Fore.RED + "Tarefa removida com sucesso!")

# Função para exibir o menu de opções com cores
def menu():
    while True:
        clear_screen()  # Limpa a tela sempre que o menu é exibido
        menu_options = [
            ["1", "Adicionar Tarefa"],
            ["2", "Visualizar Tarefas"],
            ["3", "Marcar Tarefa como Concluída"],
            ["4", "Remover Tarefa"],
            ["5", "Sair"]
        ]
        print(Fore.CYAN + "\nGerenciador de Tarefas")
        print(tabulate(menu_options, headers=[Fore.YELLOW + "Opção", Fore.YELLOW + "Descrição"], tablefmt="grid"))

        choice = input(Fore.YELLOW + "Escolha uma opção: ")

        if choice == '1':
            description = input("Descrição da nova tarefa: ")
            add_task(description)
        elif choice == '2':
            view_tarefas()
            input(Fore.YELLOW + "\nPressione Enter para voltar ao menu.")
        elif choice == '3':
            task_id = int(input("ID da tarefa a ser marcada como concluída: "))
            complete_task(task_id)
            input(Fore.YELLOW + "\nPressione Enter para voltar ao menu.")
        elif choice == '4':
            task_id = int(input("ID da tarefa a ser removida: "))
            remove_task(task_id)
            input(Fore.YELLOW + "\nPressione Enter para voltar ao menu.")
        elif choice == '5':
            print(Fore.BLUE + "Saindo do programa.")
            break
        else:
            print(Fore.RED + "Opção inválida. Tente novamente.")
            input(Fore.YELLOW + "\nPressione Enter para voltar ao menu.")

if __name__ == '__main__':
    menu()
