#
#Qual é o seu nome? ")
#t("Qual é sua idade? "))
#Aonde você mora? ")
#ct(nome = name, idade = age, cidade = city)
#
# in dict_user.items():
#er[age] >= 0:
#dict_user)
#
#
#
#
    #print("Invalid age. Please type a number.")
#except TypeError():
#    print("Invalid. Please input a correct type.")


#dict_user = {
#    "name" : "",
#    "age" : "",
#    "city" : ""
#}
#
#
#while True:
#    try:
#        dict_user['name'] = input("Qual é o seu nome? ")
#        dict_user['age'] = int(input("Qual é sua idade? "))
#        dict_user['city'] = input("Aonde você mora? ")
#            
#        number = int(dict_user["age"])
#
#        if number > 0:
#            print(f"User created successfully: \n{dict_user}")
#            break
#        else:
#            print("Informação inválida, tente novamente")
#            
#    except (ValueError, TypeError):
#        print("Invalid age. Please type a number.")
#
##chat
#dict_user = {
#    "name": "",
#    "age": "",
#    "city": ""
#}
#
## Pergunta nome e cidade UMA vez
#dict_user['name'] = input("Qual é o seu nome? ")
#dict_user['city'] = input("Aonde você mora? ")
#
## Agora fica num loop só para a idade
#while True:
#    try:
#        age = int(input("Qual é sua idade? "))
#        
#        if age <= 0:
#            print("Idade inválida. Digite um número maior que 0.")
#            continue  # volta para perguntar idade de novo
#
#        dict_user['age'] = age
#        print(f"User created successfully:\n{dict_user}")
#        break  # sai do while da idade
#
#    except (ValueError, TypeError):
#        print("Invalid age. Please type a NUMBER.")

##Exercicios

#Respostas:
#Ex: 1
#1) Eu rodei no vscode e me retornou 4,8. Mas nao entendo qual a matematica e a linha que esta acontecendo
#2) Não sei
#
#Ex:2
#1) 1 linha = Mr. Akira e 2 linha = Dr. Akira, mas eu tive que rodar no vscode para saber o que sairia na segunda linha, pois tomei base que tendo um parametro "prefix", e mesmo o usuario colocando "Dr." não alteraria o print da segunda linha e mesmo assim retornaria Mr.Akira tambem.
#2) Um parametro que vai ser padrão para qualquer entratada de informação?
#
#Ex: 3
#1) Vai aparecer "23"
#2) print("Idade encontrada:", user)

from data_engineering.python_fundamentos.desafios.utils import filter_even,safe_divide

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_nums = filter_even(numbers)
print(even_nums)



print(safe_divide(10, 2))     # deve dar 5
print(safe_divide(10, 0))     # mensagem de erro amigável
print(safe_divide("10", "a")) # mensagem de tipos inválidos
