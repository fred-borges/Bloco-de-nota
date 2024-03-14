import tkinter as tk
from tkinter.filedialog import asksaveasfilename
from tkinter import filedialog
from tkinter import messagebox 

#Iniciando a janela
root = tk.Tk()
root.geometry("400x240")
root.title("Bloco de notas")


def getTextInput():
    result = textExample.get("1.0", "end")
    print(result)

#Fechar Janela
def Sair():
    messagebox.askokcancel("askokcancel", "Desejas sair?")
    root.destroy()

#Salvar Arquivo
def salvar_arquivo():
    conteudo = textExample.get("1.0", "end-1c")
    nome_arquivo = filedialog.asksaveasfilename(defaultextension=".txt")
    if nome_arquivo:
        with open(nome_arquivo, "w") as arquivo:
            arquivo.write(conteudo)
            messagebox.showinfo("showinfo", "Arquivo salvo")
            print(f"Arquivo '{nome_arquivo}' salvo com sucesso.")


#Abrir Arquivo
def abrir_arquivo():
    # Abre a caixa de diálogo para selecionar um arquivo
    nome_arquivo = filedialog.askopenfilename()

    # Verifica se o usuário escolheu um arquivo
    if nome_arquivo:
        with open(nome_arquivo, 'r') as arquivo:
            # Lê o conteúdo do arquivo
            conteudo = arquivo.read()

            # Limpa o conteúdo atual do bloco de notas
            textExample.delete(1.0, tk.END)

            # Insere o conteúdo do arquivo no bloco de notas
            textExample.insert(tk.END, conteudo)


textExample = tk.Text(root, height=10)
textExample.pack()


btnRead = tk.Button(root, height=1, width=10, text="Ler", command=getTextInput)
btnRead.pack()



btnSave = tk.Button(root, height=1, width=10, text="Salvar", command=salvar_arquivo)
btnSave.pack()
btnSave.place(x=240,y=164)



btnOpen = tk.Button(root, height=1, width=10, text="Abrir", command=abrir_arquivo)
btnOpen.pack()
btnOpen.place(x=80,y=164)


btnExit = tk.Button(root, height=1, width=10, text="Sair", command=Sair)
btnExit.pack()
btnExit.place(x=160,y=200)
root.mainloop()