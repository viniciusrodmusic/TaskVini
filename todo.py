from tkinter import Tk, Checkbutton, Label, Button, Frame, Toplevel, Entry, messagebox
from datetime import datetime


janela = Tk()
janela.geometry("800x400")
janela.resizable(False, False)
janela.config(bg="#222729")
janela.title("Task Vini")


# FUNÇÕES


def saving_tasks(task_name):

    with open("./ToDo/tasks.txt", "a") as file:
        file.write(task_name + "\n")





def task_date():

    today = datetime.now()
    formatted_date = today.strftime("%d - %B")

    return formatted_date


def rows():
    """
    FUNÇÃO COM CLOSURE QUE ACRESCENTA 1 UNIDADE A "LINHA"
    ESSA "LINHA" SERÁ USADA PARA POSICIONAR A PRÓXIMA TASK NO GRID, SEMPRE UMA ABAIXO DA OUTRA

    RETORNA: A FUNÇÃO INTERNA incrementa_linha()

        A FUNÇÃO INTERNA RETORNA: A LINHA INCREMENTADA QUE SERÁ 
        USADA NA FUNÇÃO adding_task() PARA O POSICIONAMENTO

        LINHA -> COMEÇA EM -1 PARA QUE AO SER CHAMADA e INCREMENTADA PELA PRIMEIRA VEZ INICIE NO ÍNDICE 0
    """
    linha = -1
    def incrementa_linha():
        nonlocal linha
        linha += 1
        return linha
    return incrementa_linha

change_grid_row = rows() # CRIEI O AMBIENTE EXTERNO PARA USUFRUIR DA CLOSURE POSTERIORMENTE



def add_new_task():

    # CRIANDO UMA JANELA PARA QUE O USUARIO POSSAR INSERIR O NOME DA TASK
    new_window = Toplevel(janela, bg="#222729")
    new_window.title("What's the task name?")
    new_window.resizable(False, False)
    new_window.geometry("500x100")

    # CRIANDO O CAMPO DE ENTRADA
    task_entry = Entry(new_window)
    task_entry.pack(anchor="center", fill="x", expand=True, padx=20)

    # CRIANDO O BOTÃO DE CONFIRMAR QUE CHAMA A FUNÇÃO DE ADICIONAR TASK (adding_task)
    task_confirm = Button(new_window, text="Done", command=lambda: adding_task(new_window, task_entry), bg="gray", fg="white", activebackground="black", activeforeground="gray", highlightthickness=0, relief="flat")
    task_confirm.pack(pady=(0, 20))





def adding_task(window, entry):
    """ 
    FUNÇÃO QUE ADICIONA A NOVA TASK NA JANELA PRINCIPAL

        PARÂMETRO: 
            - windows: a janela que irá ser fechada
            - entry: o campo de entrada de texto

    CADA VEZ QUE ESTA FUNÇÃO É CHAMADA, ELA INICIALIZA row_position QUE ATUALIZA
    O NÚMERO DA LINHA PARA SER POSICIONADA NO GRID

    O SOFTWARE FOI PROJETADO PARA CABER APENAS 5 TASKS, OU SEJA
    SÓ ADICIONA OUTRA NOVA SE FOR ABAIXO DO ÍNDICE 5 -> 0 a 4
    """

    task_name = entry.get()
    window.destroy()

    row_position = change_grid_row()

    if row_position < 5:

        check = Checkbutton(frame_inferior, text=task_name, height=
        3, anchor="w", activebackground="#3C4346", bg="#101213", fg="gray", font=("Times New Roman", 15), highlightthickness=0)
        check.grid(row=row_position, column=0, sticky="nsew")

        # DATA DE CRIAÇÃO DA TASK
        date = task_date()

        data_task = Label(frame_inferior, text=date, width=12, height=3, font=("Times New Roman", 15),bg="#222729", fg="gray")
        data_task.grid(row=row_position, column=1, sticky="nsew")

        # SALVANDO A TASK EM UM ARQUIVO TXT
        saving_tasks(task_name)

    else:
        messagebox.showinfo("Information", "You can only add 5 tasks")

    













# O CONTAINER DE CIMA QUE AGRUPA O TITULO E O BOTÃO DE ADICIONAR TASK
frame_superior = Frame(janela, bg="#222729")
frame_superior.pack(fill="x")




# O TÍTULO: TASK
task = Label(frame_superior, text="Tasks", font=("Times New Roman", 20), anchor="w", fg="gray", bg="#222729")

task.pack(padx=20, pady=(30, 5), fill="x", side="left")




# O BOTÃO ADICIONAR TASK
add_task = Button(frame_superior, text="Add new task", bg="gray", highlightthickness=0, relief="flat", fg="white", activebackground="black", activeforeground="gray", command=add_new_task)

add_task.pack(side="right", padx=20, pady=(30, 5))




# O CONTAINER DE BAIXO QUE AGRUPA AS TASKS E A DATA DE CRIAÇÃO DELAS
frame_inferior = Frame(janela, bg="#2D3335")
frame_inferior.pack(fill="both", expand=True)
# DIVIDINDO ESSE CONTAINER EM LINHAS E COLUNAS -> 2 COLUNAS E 5 LINHAS
frame_inferior.grid_columnconfigure(0, weight=4)
frame_inferior.grid_columnconfigure(1, weight=1)
frame_inferior.grid_rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")







janela.mainloop()