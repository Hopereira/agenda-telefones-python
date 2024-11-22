import sqlite3
import os


class Banco:
    def __init__(self):
        # Conectando ao banco de dados
        self.conexao = sqlite3.connect(os.path.abspath("data/agenda.db"))
        self.cursor = self.conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        """Cria a tabela 'contato' caso não exista."""
        try:
            self.cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS contato (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT NOT NULL
                )
                '''
            )
            print("Tabela criada com sucesso!")
            self.conexao.commit()
        except sqlite3.Error as e:
            print(f"Erro ao criar a tabela: {e}")
            self.conexao.rollback()

    def inserir_dados(self, nome, telefone):
        """Insere um novo contato na tabela."""
        try:
            self.cursor.execute(
                '''INSERT INTO contato (nome, telefone) VALUES (?, ?)''',
                (nome, telefone)
            )
            self.conexao.commit()
            return "Dados inseridos com sucesso!"
        except sqlite3.Error as e:
            self.conexao.rollback()
            return f"Erro ao inserir os dados: {e}"

    def listar_dados(self):
        """Lista todos os contatos da tabela."""
        try:
            self.cursor.execute('''SELECT * FROM contato''')
            dados = self.cursor.fetchall()
            return dados
        except sqlite3.Error as e:
            print(f"Erro ao listar os dados: {e}")
            return []

    def fechar_conexao(self):
        """Fecha a conexão com o banco de dados."""
        self.conexao.close()
 