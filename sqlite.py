import sqlite3

# Criando o banco
banco = sqlite3.connect("primeiro_banco.db")

# Inicializando um cursor
cursor = banco.cursor()

# Criando uma tabela
cursor.execute("CREATE TABLE IF NOT EXISTS pessoas (nome text,idade intenger, email text)")

# Inserindo dados na tabela
cursor.execute("INSERT INTO pessoas VALUES ('Joao',15,'joao123@gmail.com')")

# Deletando registros

cursor.execute("DELETE from pessoas WHERE nome = 'Pedro' ")

# Commitando tudo no banco de dados
banco.commit()

# Pegando dados da tabela
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())

# Fechando o banco
banco.close()
