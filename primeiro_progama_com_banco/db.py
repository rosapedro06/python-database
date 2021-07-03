import sqlite3
from pandas_table import Tabela

class Banco:
    def __init__(self,db_name="banco_de_dados.db"):
        self.banco = sqlite3.connect(db_name)
        self.pd = Tabela()
    
    def desconecta(self):
        try:
            self.banco.close()
        except AttributeError:
            print("Conecte ao banco primeiro!")

    def tabela(self):
        try:
            cursor = self.banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS alunos (id integer primary key autoincrement,nome text,ano_escolar intenger, nota intenger)")
        except AttributeError:
            print("Conecte ao banco antes!")

    def novoAluno(self,nome,ano_escolar,nota):
        try:
            cursor = self.banco.cursor()
            try:
                cursor.execute("INSERT INTO alunos(nome,ano_escolar,nota) VALUES ('{0}',{1},{2})".format(nome,ano_escolar,nota))
                self.banco.commit()
            except sqlite3.IntegrityError:
                print("Ja existe um cliente com esse ID!")
        except AttributeError:
            print("Conecte ao banco antes!")

    def verAlunos(self):
        try:
            self.pd.verAlunos("alunos",self.banco)
        except AttributeError:
            print("Conecte ao banco antes!")

    def verAluno(self,id):
        try:
            self.pd.verAluno("alunos",id,self.banco)
        except AttributeError:
            print("Conecte ao banco antes!")

    def deletar(self,id):
        try:
            cursor = self.banco.cursor()
            cursor.execute("DELETE FROM alunos WHERE id = {0}".format(id))
            self.banco.commit()
        except AttributeError:
            print("Conecte ao banco antes!")