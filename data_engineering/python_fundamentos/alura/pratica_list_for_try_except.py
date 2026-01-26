#exercicio 1
print("Exercicio 1")
numeros = [1,2,3,4,5,6,7,8,9,10]
nomes = ["Ana", "Bruno", "Carlos", "Diana"]
ano = [2001, 2026]

#exercicio 2
print("Exercicio 2")
for numero in numeros:
    print(numero)

#exercicio 3
print("Exercicio 3")
soma_total = 0
for numero in numeros:
    if numero % 2 == 1:
        soma_total += numero
        print(f"A soma total dos numeros impares: {soma_total} ")

#exercicio 4
print("Exercicio 4")
for numero in reversed(numeros):
    print(numero)

#exercicio 5
print("Exercicio 5")
numero = int(input("Digite um numero de 1 a 10: "))
try:
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
except ValueError:
    print("Por favor, digite um número válido.")

#exercicio 6
print("Exercicio 6")
lista_numeros = input("Digite uma lista de números separados por vírgula: ")
try:
    numero = [int(num.strip()) for num in lista_numeros.split(",")]
    soma = sum(numero)
    print(f"A soma dos números na lista é: {soma}")
except ValueError:
    print("Entrada inválida. Certifique-se de digitar apenas números separados por vírgula.")

#exercicio 7
print("Exercicio 7")
lista = input("Digite uma lista de numeros separados por vírgula: ")
try:
    num_lista = [int(num.strip()) for num in lista.split(",")]
    media = sum(num_lista) / len(num_lista)
    print(f"A média dos números na lista é: {media}")
except ValueError:
    print("Entrada inválida. Certifique-se de digitar apenas números separados por vírgula.")
except ZeroDivisionError:
    print("A lista está vazia. Não é possível calcular a média.")