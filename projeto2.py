#====APP DO PROFESSOR====#
media_aprovacao = 7
alunos = []

#Função para adicionar um aluno à lista de alunos e suas respectivas notas
def adicionar_aluno():
    qtd_alunos = int(input("Quantos alunos serão adicionados?: "))
    if qtd_alunos <= 0:
        print("Insira uma quantidade de alunos maior que 0.")
    else:
        for i in range(qtd_alunos):
            nomeAluno = input('Qual aluno é?: ')
            notas = []
            for i in range(4):
                notasAluno = float(input(f'Qual é a {i+1}° nota?: '))
                notas.append(notasAluno)
            aluno = {'Nome': nomeAluno, 'Notas': notas}
            alunos.append(aluno)
            print(alunos)



def media():
    global media_aprovacao
    nova_media = float(input('Insira a nova média de aprovação: '))
    media_aprovacao = nova_media
    print(f'A nova média de aprovação dos alunos é = {media_aprovacao}')



def editar():
    menu2 = {1:"Editar nome", 2: "Editar notas", 3:"Voltar"}
    print(menu2)
    escolha2 = int(input("Seleciona uma opção: "))

    if escolha2 == 1:
        for i in alunos:
            print(i['Nome'])
        editar_aluno = input("Qual aluno você deseja editar?: ")
        for i in alunos:
            if editar_aluno != i['Nome']:
                print("Insira um nome dentro da lista dos alunos, por favor.")
            else:
                novoNome = input(f"Insira um nome novo para o aluno {i['Nome']}: ")
                i['Nome'] = novoNome

    elif escolha2 == 2:
        for i in alunos:
            print(i['Nome'])
        editar_notas = input("De qual aluno você deseja editar as notas?: ")
        for i in alunos:
            if editar_notas == i['Nome']:
                for j, nota in enumerate(i['Notas']):
                    print(f"{j+1}° nota: {nota}")
                escolha_nota = int(input("Que nota voce deseja editar?: "))
                if escolha_nota <= 0 or escolha_nota >= 5: #tratativa de erro caso o usuario nao escolha uma das 4 notas
                    print("Escolha uma das 4 notas para editar.")
                else:
                    ind = escolha_nota - 1
                    print(i['Notas'][ind])
                    nova_nota = float(input("Insira uma nova nota: "))
                    if nova_nota < 0 or nova_nota > 10:
                        print("Insira um valor de 0 a 10.")
                    else:
                        nota = i['Notas'][ind] = nova_nota #A variável nota é apenas para me auxiliar no print, acredito que ficou um pouco mais organizado, mesmo sendo desnecessária
                        print(f"A nota atualizada agora é: {nota}")
            else:
                print("Insira um nome válido dentro da lista de alunos.")

    elif escolha2 == 3:
        print("Saindo da opção de edição de alunos.")

    else:
        print("Selecione uma opção válida no menu, por favor.")



def calcular_media():
    for aluno in alunos:
        print(aluno['Notas'])
        media = sum(aluno['Notas']) / len(aluno['Notas'])
        print(f"Aluno(a): {aluno['Nome']}")
        print(f"Média: {media}")
        if media >= media_aprovacao:
            print(f"Aluno(a) {aluno['Nome']} está aprovado.")
        elif media > media_aprovacao -1 and media < media_aprovacao:
            print(f"Aluno(a) {aluno['Nome']} está de recuperação.")
        else:
            print(f"Aluno(a) {aluno['Nome']} está reprovado na matéria.")



while True:
    menu = ['1- Adicionar aluno; ',
            '2- Definir média de aprovação; ',
            '3- Editar aluno; ',
            '4- Calcular médias; ',
            '5- Sair do aplicativo']


    print('===APP DO PROFESSOR===')
    for opcao in menu:
        print(opcao)
    try:
        escolha = int(input('Selecione uma opção: '))
    except ValueError:
        print('Escolha apenas valores numéricos existentes no MENU.')
        continue

    if escolha == 1:
        adicionar_aluno()

    if escolha == 2:
        media()

    if escolha == 3:
        editar()

    if escolha == 4:
        calcular_media()


    if escolha == 5:
        print("Obrigado por selecionar nosso gerenciador de notas! Até a próxima.")
        break
