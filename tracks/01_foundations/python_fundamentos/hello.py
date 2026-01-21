#nome = "vitor" #String
#idade = 23 #int
#altura = 1.75 #Float
#area = "Dados" #String
#
#
#print("Meu nome é", nome)
#print("Minha idade é", idade)
#print("Minha altura é", altura)
#print("Minha area de atuação é", area)
#
#print(f'Meu nome é {nome}, tenho {idade} anos, e sou alto com {altura}')
#
#pergunta = input("Qual é o seu nome? ")
#print(f"O nome do usuário é {pergunta}")
#----------------------------------------------#
##Desafio 1

#pergunta_nome = input("Qual é o seu nome? ")
#pergunta_area = input("Qual área você trabalha? ")
#print(f"Nome do usuário: {pergunta_nome} e Área de atuação: {pergunta_area}")

##Desafio 2

#name = input("Qual seu nome? ")
#vacation = input("Qual sua área de atuação? ")
#age = int(input("Qual a sua idade? "))
#fez_aniversario = input("Você já fez aniversário este ano? Responda apenas 's' ou 'n') ")
#resposta = fez_aniversario.lower()
#ano_atual = 2025
#
#print(f"Seu nome é {name}, você trabalha com {vacation} e sua idade é {age}")
#print(f"Daqui 10 anos você terá {age + 10} anos")
#
## = serve para guardar um valor em uma variavel
## == operador de comparação
#
#if resposta == 's':
#    print(f"Você nasceu no ano de {ano_atual - age}")
#elif resposta == 'n':
#    print(f"Você nasceu no ano de {ano_atual - age - 1}")
#else:
#    print("Respota inválida")
#--------------------------------------------------------------------#
##Desafio 3

#hobbies = []

#print("Coloque abaixo seus 3 hobbies favoritos!")
#print("-------------------------------")
##pergunta_hobbies1 = input("Primeiro hobbie? ")
##hobbies.append(pergunta_hobbies1)
##
##pergunta_hobbies2 = input("Segundo hobbie? ")
##hobbies.append(pergunta_hobbies2)
##
##pergunta_hobbies3 = input("Terceiro hobbie? ")
##hobbies.append(pergunta_hobbies3)
#
#for i in range(3):
#    pergunta_hobbies = input(f"Hobbie {i+1}: ")
#    hobbies.append(pergunta_hobbies)
#print(f"Seus hobbies são: {hobbies}")
#
#for hobbie in hobbies:
#    print("->", hobbie)

##mini-desafio

#numeros = [10,5,7,3]
#soma = 0
#
#for n in numeros:
#    #n = sum(numeros)
#    #numeros.append(soma)
#    soma+=n
#    #soma=soma+n
#    #n = n + soma
#    print(soma)


#soma = 0 
#
#while True:
#    numero = int(input("Digite um número (0 para sair): "))
#    soma += numero
#    print(soma)
#    if numero == 0:
#        break


##Desafio - Funções

#def calcular_soma(lista_numeros):
#    #lista_numeros = []
#    soma = 0
#    for n in lista_numeros:
#        soma += n
#    return soma
#        
#        
#resultado = calcular_soma([10,5,7,3])
#print(f"O resultado total é: {resultado}")

#client = {
#    "name" : "",
#    "age" : "",
#    "city" : "",
#    "profession" : ""
#}
#
##for key, value in client.items():
##    nome = input("Digite seu nome: ")
##    client["name"] = nome
##    idade = int(input("Digite sua idade: "))
##    client["age"] = idade
##    cidade = input("Qual é a sua cidade: ")
##    client["city"] = cidade
##    profissao = input("Qual a sua profissão: ")
##    client["profession"] = profissao
##    print(client)
##    break
#
#client["name"] = input("Digite seu nome: ")
#client["age"] = int(input("Digite sua idade: "))
#client["city"] = input("Qual é a sua cidade: ")
#client["profession"] = input("Qual a sua profissão: ")
#
#print(client)
#
#for chave, valor in client.items():
#    print(f"{chave}: {valor}")


list_clients = []

while True:
    add_users = input("Cadastrar novos usuários?").lower()
    if add_users == 'sair':
        break

    elif add_users == 's' or add_users == 'sim':
        name = input("Digite seu nome: ")
        age = int(input("Digite sua idade: "))
        city = input("Digite a cidade: ")
    new_user = {
        'name' : name,
        'age' : age,
        'city' : city
    }
    list_clients.append(new_user)
    print(list_clients)
print("--- CLIENTES CADASTRADOS ---")
for list_client in list_clients:
    nome = list_client['name']
    idade = list_client['age']
    cidade = list_client['city']
    print(f"{nome} | {idade} | {cidade}")