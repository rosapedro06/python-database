import sqlite3
from pandas_table import Tabela

class Banco:
    """
    Classe para inicializar o Banco de dados com funções de Crud
    """
    def __init__(self,db_name="banco_de_dados.db"):
        """
        Função inicial para inicializar o banco e o Pandas
        """
        self.banco = sqlite3.connect(db_name)
        self.pd = Tabela()
    
    def desconecta(self):
        """
        Fecha o banco de dados
        """
        try:
            self.banco.close()
        except AttributeError:
            print("Conecte ao banco primeiro!")

    def tabela(self):
        """
        Cria a tabela
        """
        try:
            cursor = self.banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS alunos (id integer primary key autoincrement,nome text,ano_escolar intenger, nota intenger)")
        except AttributeError:
            print("Conecte ao banco antes!")

    def novoAluno(self,nome,ano_escolar,nota):
        """
        Adiciona um aluno
        """
        try:
            cursor = self.banco.cursor()
            try:
                cursor.execute("INSERT INTO alunos(nome,ano_escolar,nota) VALUES ('{0}',{1},{2})".format(nome,ano_escolar,nota))
                self.banco.commit()
                # Verifica erro de integridade caso ja tenha um id cadastrado.
            except sqlite3.IntegrityError:
                print("Ja existe um cliente com esse ID!")
        except AttributeError:
            print("Conecte ao banco antes!")

    def verAlunos(self):
        """
        Ve todos os alunos cadastrados utilizando o Pandas
        """
        try:
                self.pd.verAlunos("alunos",self.banco)
        except AttributeError:
            print("Conecte ao banco antes!")

    def verAluno(self,id):
        """
        Ve um aluno em especifico também utilizando o pandas
        """
        try:
            self.pd.verAluno("alunos",id,self.banco)
        except AttributeError:
            print("Conecte ao banco antes!")
    
    def atualizaAluno(self,id,nome,serie,nota):
        """
        Atualiza um aluno
        """
        try:
            cursor = self.banco.cursor()
            try:
                cursor.execute("UPDATE alunos SET nome='{0}',ano_escolar={1},nota={2} WHERE id={3}".format(nome,serie,nota,id))
                self.verAluno(id)
                self.banco.commit()
            except sqlite3.IntegrityError:
                print("Erro ao achar aluno!")
        except AttributeError:
            print("Conecte ao banco antes!")

    def deletar(self,id):
        """
        Deleta um aluno
        """
        try:
            cursor = self.banco.cursor()
            cursor.execute("DELETE FROM alunos WHERE id = {0}".format(id))
            self.banco.commit()
        except AttributeError:
            print("Conecte ao banco antes!")