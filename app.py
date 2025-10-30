import tkinter as tk
from tkinter import messagebox

usuarios = []

def login():
    login = tk.Tk()
    login.title("Logar")
    login.geometry("400x400")

    tituloLogin_label = tk.Label(login, text="Logar-se", font=("arial", 14, "bold"))
    tituloLogin_label.pack(padx=10,pady=10)

    usuario_label = tk.Label(login, text="Coloque o nome do usuário:")
    usuario_label.place(x=10,y=50)

    senhaLogin_label = tk.Label(login, text="Coloque sua senha:")
    senhaLogin_label.place(x=10,y=120)

    usuarioLogin_entry = tk.Entry(login, width=60)
    usuarioLogin_entry.place(x=10, y=90)

    senhaLogin_entry = tk.Entry(login, width=60)
    senhaLogin_entry.place(x=10, y=160)

    entrarLogin = tk.Button(login, text="Entrar", width=50)
    entrarLogin.place(x=10,y=200)

    login.mainloop()

janela = tk.Tk()
janela.title("Login de usuários em txt")
janela.geometry("800x400")

titulo = tk.Label(text="Modelo de registro em txt", font=("arial", 14, "bold"))
titulo.pack(padx=10,pady=10)

login_label = tk.Label(text="Logar usuário")
login_label.place(x=80,y=100)

registrar_label = tk.Label(text="Registrar")
registrar_label.place(x=650,y=100)

login_button = tk.Button(text="login", width=20, command=login)
login_button.place(x=50,y=140)

registrar_button = tk.Button(text="Registrar", width=20)
registrar_button.place(x=600,y=140)

janela.mainloop()