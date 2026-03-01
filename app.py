import tkinter as tk
from tkinter import messagebox

ARQUIVO = "usuarios.txt"

def salvar_usuario(nome, email, senha):
    with open(ARQUIVO, "a") as f:
        f.write(f"{nome};{email};{senha}\n")

def verificar_login(nome, senha):
    try:
        with open(ARQUIVO, "r") as f:
            for linha in f:
                dados = linha.strip().split(";")
                if dados[0] == nome and dados[2] == senha:
                    return dados
    except FileNotFoundError:
        return None
    return None

def tela_principal(dados_usuario):
    tela = tk.Tk()
    tela.title("Tela Principal")
    tela.geometry("400x300")

    tk.Label(tela, text="Bem-vindo!", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(tela, text=f"Nome: {dados_usuario[0]}").pack()
    tk.Label(tela, text=f"Email: {dados_usuario[1]}").pack()
    tk.Label(tela, text=f"Senha: {dados_usuario[2]}").pack()

    tk.Button(tela, text="Sair", command=tela.destroy).pack(pady=20)

    tela.mainloop()

def login():
    login_janela = tk.Tk()
    login_janela.title("Login")
    login_janela.geometry("400x300")

    tk.Label(login_janela, text="Login", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Label(login_janela, text="Usuário:").pack()
    usuario_entry = tk.Entry(login_janela)
    usuario_entry.pack()

    tk.Label(login_janela, text="Senha:").pack()
    senha_entry = tk.Entry(login_janela, show="*")
    senha_entry.pack()

    def entrar():
        nome = usuario_entry.get()
        senha = senha_entry.get()
        dados = verificar_login(nome, senha)

        if dados:
            messagebox.showinfo("Sucesso", "Login realizado!")
            login_janela.destroy()
            tela_principal(dados)
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos")

    tk.Button(login_janela, text="Entrar", command=entrar).pack(pady=10)

    login_janela.mainloop()

def registrar():
    reg_janela = tk.Tk()
    reg_janela.title("Registrar")
    reg_janela.geometry("400x350")

    tk.Label(reg_janela, text="Registrar", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Label(reg_janela, text="Email:").pack()
    email_entry = tk.Entry(reg_janela)
    email_entry.pack()

    tk.Label(reg_janela, text="Usuário:").pack()
    usuario_entry = tk.Entry(reg_janela)
    usuario_entry.pack()

    tk.Label(reg_janela, text="Senha:").pack()
    senha_entry = tk.Entry(reg_janela, show="*")
    senha_entry.pack()

    def cadastrar():
        nome = usuario_entry.get()
        email = email_entry.get()
        senha = senha_entry.get()

        if nome and email and senha:
            salvar_usuario(nome, email, senha)
            messagebox.showinfo("Sucesso", "Usuário cadastrado!")
            reg_janela.destroy()
        else:
            messagebox.showerror("Erro", "Preencha todos os campos")

    tk.Button(reg_janela, text="Cadastrar", command=cadastrar).pack(pady=15)

    reg_janela.mainloop()

def main():
    janela = tk.Tk()
    janela.title("Sistema de Login TXT")
    janela.geometry("400x200")

    tk.Label(janela, text="Sistema de Login", font=("Arial", 14, "bold")).pack(pady=20)

    tk.Button(janela, text="Login", width=20, command=login).pack(pady=5)
    tk.Button(janela, text="Registrar", width=20, command=registrar).pack(pady=5)

    janela.mainloop()

if __name__ == "__main__":
    main()