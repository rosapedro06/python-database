from db import Banco
import os

os.system('cls||clear')

while True:
    escolha_menu = input('Olá bem vindo ao sistema escolha uma opção: \n(1) Cadastrar um novo Aluno \n(2) Ver alunos cadastrados \n(3) Ver um aluno em especifico \n(4) Deletar um aluno \n(5) Atualizar um aluno \n(6) Sair \n -> ')

    escolha_menu = int(escolha_menu)
    # Inicia modelo
    db = Banco()
    # Desliga o sistema
    if escolha_menu == 6:
        db.desconecta()
        break

            # Cadastra um aluno
    if escolha_menu == 1:
        # Limpa o terminal
        os.system('cls||clear')
        nome_aluno = str(input("Digite o nome do aluno: "))
        ano_aluno = int(input("Digite a série do aluno: "))
        nota_aluno = int(input("Digite a nota do aluno (0-100) : "))

        # Faz a verificação das informações para evitar quebra de sistema.
        if nome_aluno == "" or  ano_aluno == 0 or ano_aluno >= 20 or nota_aluno >= 101:
            os.system('cls||clear')
            print("*"*20)
            print("Insira valores validos!")
            print("*"*20)
        else:
            os.system('cls||clear')
            # Chama a função do modelo 
            db.novoAluno(nome_aluno,ano_aluno,nota_aluno)
            print("*"*20)
            print("Aluno cadastrado com sucesso!")
            print("*"*20)
    # Ver todos os alunos
    elif escolha_menu == 2:
        os.system('cls||clear')
        print("*"*25)
        db.verAlunos()
        print("*"*25)
    # Ver apenas um aluno
    elif escolha_menu == 3:
        os.system('cls||clear')
        id_aluno_escolha = int(input("Digite o ID do aluno: "))

        # Bloco try * except para verificar a integridade do ID
        try:
            os.system('cls||clear')
            print("*"*20)
            # Chama a função porem agora com ID
            db.verAluno(id_aluno_escolha)
            print("*"*20)
        except:
            os.system('cls||clear')
            print("*"*20)
            print("Não encontramos um aluno com esse ID cadastrado!")
            print("*"*20)
    # Deleta um aluno
    elif escolha_menu == 4:
        id_aluno_escolha = int(input("Digite o ID do aluno: "))
        # Tenta achar um aluno com o ID digitado e deletalo
        try:
            os.system('cls||clear')
            db.deletar(id_aluno_escolha)
            print("*"*20)
            print("Aluno deletado com sucesso!")
            print("*"*20)
        except:
            os.system('cls||clear')
            print("*"*20)
            print("Não encontramos um aluno com esse ID cadastrado!")
            print("*"*20) 
    # Atualiza um aluno 
    elif escolha_menu == 5:
        # Mesmo sistema de criar um aluno porém mudando o método e adicionando o ID
        try:
            os.system('cls||clear')
            id_aluno = int(input("Digite o ID do aluno: "))
            nome_aluno = str(input("Digite o nome do aluno: "))
            ano_aluno = int(input("Digite a série do aluno: "))
            nota_aluno = int(input("Digite a nota do aluno (0-100) : "))

            if id_aluno == 0 or nome_aluno == "" or  ano_aluno == 0 or ano_aluno >= 20 or nota_aluno >= 101:
                os.system('cls||clear')
                print("*"*20)
                print("Insira valores validos!")
                print("*"*20)
            else:
                os.system('cls||clear')
                db.atualizaAluno(id_aluno,nome_aluno,ano_aluno,nota_aluno)
                print("*"*20)
                print("Aluno atualizado com sucesso!")
                print("*"*20)
        except:
            os.system('cls||clear')
            print("*"*20)
            print("Não encontramos um aluno com esse ID cadastrado!")
            print("*"*20) 
    elif escolha_menu >= 7:
        print("Insira uma opção valida!")
        