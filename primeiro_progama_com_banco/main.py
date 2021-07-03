from db import Banco

while True:
    escolha_menu = input('Olá bem vindo ao sistema escolha uma opção: \n(1) Cadastrar um novo Aluno \n(2) Ver alunos cadastrados \n(3) Ver um aluno em especifico \n(4) Deletar um aluno \n (5) Sair \n: ')

    escolha_menu = int(escolha_menu)

    db = Banco()
            
    if escolha_menu == 5:
        break

    if escolha_menu == 1:
        nome_aluno = str(input("Digite o nome do aluno: "))
        ano_aluno = int(input("Digite a série do aluno: "))
        nota_aluno = int(input("Digite a nota do aluno (0-100) : "))

        if nome_aluno == "" or  ano_aluno == 0 or ano_aluno >= 20 or nota_aluno >= 101:
            print("*"*20)
            print("Insira valores validos!")
            print("*"*20)
        else:
                db.novoAluno(nome_aluno,ano_aluno,nota_aluno)
                print("*"*20)
                print("Aluno cadastrado com sucesso!")
                print("*"*20)
    elif escolha_menu == 2:
        print("*"*25)
        db.verAlunos()
        print("*"*25)
    elif escolha_menu == 3:
        id_aluno_escolha = int(input("Digite o ID do aluno: "))
        try:
            print("*"*20)
            db.verAluno(id_aluno_escolha)
            print("*"*20)
        except:
            print("*"*20)
            print("Não encontramos um aluno com esse ID cadastrado!")
            print("*"*20)
    elif escolha_menu == 4:
        id_aluno_escolha = int(input("Digite o ID do aluno: "))
        try:
            db.deletar(id_aluno_escolha)
            print("*"*20)
            print("Aluno deletado com sucesso!")
            print("*"*20)
        except:
            print("*"*20)
            print("Não encontramos um aluno com esse ID cadastrado!")
            print("*"*20) 
    elif escolha_menu >= 6:
        print("Insira uma opção valida!")