from tkinter import Tk, Checkbutton, Label, Button, Frame, Toplevel, Entry

janela = Tk()
janela.geometry("800x400")
janela.resizable(False, False)
janela.config(bg="#222729")
janela.title("Task Vini")




# FUNÇÕES

def rows():
    """
    FUNÇÃO COM CLOSURE QUE ACRESCENTA 1 UNIDADE A "LINHA"
    ESSA "LINHA" SERÁ USADA PARA POSICIONAR A PRÓXIMA TASK NO GRID, SEMPRE UMA ABAIXO DA OUTRA

    RETORNA: A FUNÇÃO INTERNA incrementa_linha()
    
        A FUNÇÃO INTERNA RETORNA A LINHA INCREMENTADA QUE SERÁ 
        USADA NA FUNÇÃO adding_task() PARA O POSICIONAMENTO
    """
    linha = 0
    def incrementa_linha():
        nonlocal linha
        linha += 1
        return linha
    return incrementa_linha

change_grid_row = rows() # CRIEI O AMBIENTE EXTERNO PARA USUFRUIR DA CLOSURE POSTERIORMENTE







def add_new_task():

    # CRIANDO UMA JANELA PARA QUE O USUARIO POSSAR INSERIR O NOME DA TASK
    type_task = Toplevel(janela, bg="#222729")
    type_task.title("What's the task name?")
    type_task.resizable(False, False)
    type_task.geometry("500x100")

    # CRIANDO O CAMPO DE ENTRADA
    task_entry = Entry(type_task)
    task_entry.pack(anchor="center", fill="x", expand=True, padx=20)

    # CRIANDO O BOTÃO DE CONFIRMAR
    task_confirm = Button(type_task, text="Done", command=lambda: task_added(type_task, task_entry))
    task_confirm.pack()



def task_added(window, entry):
    """ FUNÇÃO DO BOTÃO DE CONFIRMAR

    É CHAMADA APÓS O USUÁRIO DIGITAR O NOME DA TASK, 
    ELA IRÁ CAPTURAR O VALOR DE ENTRADA PARA SER ADICIONADO NA JANELA PRINCIPAL E
    FECHAR A JANELA DE ENTRADA

    RECEBE A PROPRIA JANELA PAI COMO PARÂMETRO E O CAMPO DE ENTRADA(ENTRY)
    """

   
    task_name = entry.get()
    window.destroy()

    # CHAMA A FUNÇÃO QUE ADICIONA A TASK NA JANELA PRINCIPAL
    adding_task(task_name)





def adding_task(task_name):

    check = Checkbutton(frame_inferior, text=task_name, height=
    3, anchor="w", activebackground="#3C4346", bg="#101213", fg="gray", font=("Times New Roman", 15), highlightthickness=0)
    check.grid(row=change_grid_row(), column=0, sticky="nsew")

    






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




# A TASK EM SI
# check = Checkbutton(frame_inferior, text="task_name", height=
# 3, anchor="w", activebackground="#3C4346", bg="#101213", fg="gray", font=("Times New Roman", 15), highlightthickness=0)
# check.grid(row=0, column=0, sticky="nsew")




# DATA DE CRIAÇÃO DA TASK
data_task = Label(frame_inferior, text="25 de jul", width=12, height=3, font=("Times New Roman", 15),bg="#222729", fg="gray")
data_task.grid(row=0, column=1, sticky="nsew")




janela.mainloop()