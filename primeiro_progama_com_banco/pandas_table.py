import pandas as pd

class Tabela:
    def verAlunos(self,tabela,banco):
        df = pd.read_sql_query("SELECT * FROM {};".format(tabela),banco)
        print(df)

    def verAluno(self,tabela,id,banco):
        df = pd.read_sql_query("SELECT * FROM {0} WHERE id={1}".format(tabela,id),banco)
        print(df)