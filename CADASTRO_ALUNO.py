''' Vizualizando o codigo antes

1. Adicionar Aluno
2. Calcular Média de Notas
3. Exibir Alunos Aprovados
4. Sair
Escolha uma opção: 1

Nome: João
Idade: 16
Nota 1: 7
Nota 2: 8
Nota 3: 6

Aluno João adicionado com sucesso!

1. Adicionar Aluno
2. Calcular Média de Notas
3. Exibir Alunos Aprovados
4. Sair
Escolha uma opção: 2

Digite o nome do aluno para calcular a média: João
Média de João: 7.0
'''
nome = ""
idade = 0

print(" ==                           LEMBRETE!                           == "
    "\n ==             Cadastre-se para as informações posteriores!      == ")

while True:
    print(" ")
    print("1. Adicionar Aluno"
        "\n2. Calcular Média de Notas"
        "\n3. Exibir se o aluno está Aprovado"
        "\n4. Sair")
    opcao = int(input("Selecione uma Opção: "))
    print(" ")

    match opcao:
        case 1:
            print("OK! Vamos fazer o seu cadastro! ")
            nome = str(input("Digite o nome: "))
            idade = int(input("Digite a idade: "))
            nota1 = float(input("Digite a nota do cp1: "))
            nota2 = float(input("Digite a nota do cp2: "))
            nota3 = float(input("Digite a nota do cp3: "))
            if (nota1 >= 0 and nota1 <= 10) and (nota2 >= 0 and nota2 <= 10) and (nota3 >= 0 and nota3 <= 10):

                print("Aluno {} Cadastrado !!!".format(nome))
                print("=========================================")
                print("Se desejar saber a media basta digitar 2")
                print(" ")
            else:
                print("Digite uma nota de 0 até 10! ")
                print(" ")

        case 2:
            if (nota1 >= 0) and (nota2 >= 0) and (nota3 >= 0):
                print("Certo vamos calcular sua media!! ")

                media = (nota1 + nota2 + nota3) /3

                print("Sua media é {:.2f}".format(media))
                print(" ")

        case 3:
            #Recebe a variavel mesmo se ele nao digitar 2

            media = (nota1 + nota2 + nota3) / 3
            if (media >= 0) and (media <= 5):
                print("{} você está Reprovado !".format(nome))

            elif (media > 5) and (media <= 7):
                print("{} você está de recuperação !".format(nome))

            elif (media > 7 ) and (media <= 10):
                print("{} você está Aprovado ! PARABENS !!!!".format(nome))

            else:
                print("Erro 404#")
                print(" ")

        case 4:
            print("SAINDO .....")
            break

        case _:
            print("Digite uma opção dentre as mostradas !")
