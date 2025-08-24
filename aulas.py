
alunos = []

def cadastro_aluno():


    aluno = {}

    nome_aluno = input("Qual o nome completo do aluno?  ")

    aluno["nome"] = nome_aluno

    idade_aluno = int(input(f"Quantos anos o {nome_aluno} tem?    "))

    aluno["idade"] = idade_aluno

    nota = float(input(f"Qual a nota do {nome_aluno}?   "))
    
    aluno["nota"] = nota

    if nota >= 7:

        aprov = "Aprovado"

    
    elif 5 <= nota < 7:

        aprov = "Recuperação"
    
    elif nota < 5:

        aprov = "Reprovado"
    
    else:
        aprov = "erro"
    
    aluno["aprovacao"] = aprov

    return aluno

def formatar_aluno(aluno):
    return f"Nome: {aluno['nome']} - Idade: {aluno['idade']} - Nota: {aluno['nota']} - Aprovação: {aluno['aprovacao']}"

def calcular_media():

    total_nota = 0
    for i in alunos:
        
        total_nota += i['nota']


    media = total_nota / len(alunos)

    return media


       
while True:
    
    menu = int(input("--- PAINEL PRINCIPAL ------ \n1 → Cadastrar aluno \n2 → Listar todos os alunos \n3 → Buscar aluno por nome \n4 → Mostrar média das notas da turma \n5 → Sair \nR:"))

    

    if menu == 5:

        print("Sistema encerrado.")
    

    
    elif menu == 1:
       
       novo = cadastro_aluno()

       alunos.append(novo)


        
    elif menu == 2:

       for a in alunos:
           print(formatar_aluno(a))

    elif menu == 3:

        busca = input("Qual nome do aluno? ").lower()

        encontrado = False

        for a in alunos:

            nome = a['nome'].lower()
           

            if nome == busca:
                print(f"Nome: {a['nome']} - Idade: {a['idade']} - Nota: {a['nota']} - Aprovação: {a['aprovacao']}")
                encontrado = True
                break
        
        if not encontrado:
            print("Aluno não encontrado ou não cadastrado. Tentar novamente.")
            

    elif menu == 4:

        print(f"A média dos aulos é de {calcular_media()}")

    
    else:

        print("Opção inválida, tente novamente.")
             

             


            





    
    


    
    
