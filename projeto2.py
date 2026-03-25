#====APP DO PROFESSOR====#
media_aprovacao = 6
alunos = []

#Função para adicionar um aluno à lista de alunos e suas respectivas notas
def adicionar_aluno():
    nomeAluno = input('Qual aluno é?: ')
    notas = []
    for i in range(4):
        notasAluno = float(input(f'Qual é a {i+1}° nota?: '))
        notas.append(notasAluno)
    aluno = {'Nome': nomeAluno, 'Notas': notas}
    alunos.append(aluno)
    print(alunos)
    pass

def media():
    global media_aprovacao
    nova_media = float(input('Insira a nova média de aprovação: '))
    media_aprovacao = nova_media
    print(f'A nova média de aprovação dos alunos é = {media_aprovacao}')
    pass

def editar():
    menu2 = {1:"Editar nome", 2: "Editar notas", 3:"Voltar"}
    print(menu2)
    escolha2 = int(input("Seleciona uma opção: "))
    if escolha2 == 1:
        for i in alunos:
            print(i['Nome'])
        editar_aluno = input("Qual aluno você deseja editar?: ")
        for i in alunos:
            if editar_aluno == i['Nome']:
                novoNome = input(f"Insira um nome novo para o aluno {i['Nome']}: ")
                i['Nome'] = novoNome



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

    if escolha == 5:
        print("Obrigado por selecionar nosso gerenciador de notas! Até a próxima.")
        break
