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



textExample = tk.Text(root, height=10)
textExample.pack()





btnSave = tk.Button(root, height=1, width=10, text="Salvar", command=salvar_arquivo)
btnSave.pack()
btnSave.place(x=240,y=164)



btnOpen = tk.Button(root, height=1, width=10, text="Abrir")
btnOpen.pack()
btnOpen.place(x=80,y=164)


btnExit = tk.Button(root, height=1, width=10, text="Sair", command=Sair)
btnExit.pack()
btnExit.place(x=160,y=200)
root.mainloop()