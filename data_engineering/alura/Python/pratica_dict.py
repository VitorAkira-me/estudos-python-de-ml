#exercicio 1
info_pessoa = [{
    "nome": "Vitor",
    "idade": 25,
    "cidade": "São Paulo"}, 
    {
    "nome": "Ana",
    "idade": 30,
    "cidade": "Rio de Janeiro"}, 
    {
    "nome": "Carlos",
    "idade": 28,
    "cidade": "Belo Horizonte"}]

#exercicio 2
for pessoa in info_pessoa:
    print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Cidade: {pessoa['cidade']}")
    pessoa_escolha = input("Deseja atualizar a idade dessa pessoa? (s/n): ").lower()
    if pessoa_escolha == 's':
        nova_idade = int(input(f"Digite a nova idade de {pessoa['nome']}: "))
        pessoa['idade'] = nova_idade
        print(f"Idade de {pessoa['nome']} atualizada para {nova_idade}.")
        print(pessoa)
    
    profissao = input(f"Deseja adicionar a profissão de {pessoa['nome']}? (s/n): ").lower()
    if profissao == 's':
        nova_profissao = input(f"Digite a profissão de {pessoa['nome']}: ")
        pessoa['profissao'] = nova_profissao
        print(f"Profissão de {pessoa['nome']} adicionada: {nova_profissao}.")
        print(pessoa)

    remover = input(f"Deseja remover um item do dicionario de {pessoa['nome']}? (s/n): ").lower()
    if remover == 's':
        item_remover = input("Digite o nome do item que deseja remover (nome, idade, cidade, profissao): ").lower()
        if item_remover in pessoa:
            del pessoa[item_remover]
            print(f"Item '{item_remover}' removido do dicionario de {pessoa['nome']}.")
            print(pessoa)
    break

#exercicio 3
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

#exercicio 4
pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")

#exercicio 5
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)