import pandas as pd

class Tabela:
    """
    Classe do pandas para automatizar a criação das tabelas do sistema
    """
    def verAlunos(self,tabela,banco):
        """
        Le os alunos do banco e retorna em uma tabela
        """
        df = pd.read_sql_query("SELECT * FROM {};".format(tabela),banco)
        print(df)

    def verAluno(self,tabela,id,banco):
        """
        Le um aluno do banco e retorna em uma tabela
        """
        df = pd.read_sql_query("SELECT * FROM {0} WHERE id={1}".format(tabela,id),banco)
        print(df)