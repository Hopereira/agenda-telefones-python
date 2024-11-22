import customtkinter as ctk
from tkinter import messagebox
import sys
import os
caminho_projeto = os.path.abspath(os.path.dirname(__file__))
caminho_data = os.path.join(caminho_projeto, "../data")
sys.path.append(caminho_data)
from banco import Banco



# Criando classe MainView
janela = ctk.CTk()

class MainView:
    def __init__(self):  # Construtor
        self.janela = janela
        self.banco = Banco()  # Instanciando o banco de dados
        self.janela_principal()
        self.janela.mainloop()

    def janela_principal(self):
        self.janela.geometry("400x300")
        self.janela.title("Agenda")
        self.janela.resizable(False, False)

        # Título da janela
        ctk.CTkLabel(
            master=janela,
            text="Agenda",
            font=("Roboto", 20),
            text_color="#00b0f0",
        ).place(x=25, y=10)

        # Título "Entre com o nome"
        ctk.CTkLabel(
            master=janela,
            text="Entre com o nome",
            font=("Roboto", 14),
            text_color="#00b0f0",
        ).place(x=140, y=60)

        # Entrada de texto para nome
        self.nome_Entrada = ctk.CTkEntry(
            master=janela, width=300, placeholder_text="Nome", font=("Roboto", 14)
        )
        self.nome_Entrada.place(x=50, y=90)

        # Título "Entre com o telefone"
        ctk.CTkLabel(
            master=janela,
            text="Entre com o telefone",
            font=("Roboto", 14),
            text_color="#00b0f0",
        ).place(x=140, y=120)

        # Entrada de texto para telefone
        self.telefone_Entrada = ctk.CTkEntry(
            master=janela, width=300, placeholder_text="Telefone", font=("Roboto", 14)
        )
        self.telefone_Entrada.place(x=50, y=150)

        # Botão salvar
        botao_salvar = ctk.CTkButton(
            master=self.janela,
            text="Salvar",
            font=("Roboto", 14),
            command=self.salvar_dados  # Chama a função ao clicar
        )
        botao_salvar.place(x=200, y=200)

        # Botão listar
        botao_listar = ctk.CTkButton(
            master=self.janela,
            text="Listar",
            font=("Roboto", 14),
            command=self.listar_dados  # Chama a função ao clicar
        )
        botao_listar.place(x=50, y=200)

    def salvar_dados(self):
        """Salva os dados no banco."""
        nome = self.nome_Entrada.get()
        telefone = self.telefone_Entrada.get()

        if not nome or not telefone:
            messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos!")
            return

        mensagem = self.banco.inserir_dados(nome, telefone)
        messagebox.showinfo("Informação", mensagem)

        # Limpa os campos após salvar
        self.nome_Entrada.delete(0, "end")
        self.telefone_Entrada.delete(0, "end")

    def listar_dados(self):
        """Exibe os dados cadastrados."""
        dados = self.banco.listar_dados()
        if not dados:
            messagebox.showinfo("Informação", "Nenhum dado encontrado.")
            return

        # Janela para exibir os contatos
        janela_listagem = ctk.CTkToplevel(self.janela)
        janela_listagem.geometry("400x300")
        janela_listagem.title("Contatos")

        # Adiciona os contatos na nova janela
        texto = "ID\tNOME\tTELEFONE\n"
        texto += "\n".join([f"{id_}\t{nome}\t{telefone}" for id_, nome, telefone in dados])

        ctk.CTkLabel(
            master=janela_listagem,
            text=texto,
            font=("Roboto", 14),
            justify="left",
        ).pack(pady=10)


if __name__ == "__main__":
    MainView()
       

   