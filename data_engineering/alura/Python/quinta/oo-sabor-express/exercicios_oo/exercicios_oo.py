from dataclasses import dataclass

#class musica:
#    def __init__(self, nome: str, artista: str, duracao: int):
#        self.nome = nome
#        self.artista = artista
#        self.duracao = duracao
#
#n = musica('From The Inside', 'Linkin Park', 176)
#print(vars(n))
##Ao instanciar a classe musica, um objeto é criado e o método __init__ atribui valores aos seus atributos.
##Ao chamar musica('From The Inside', 'Linkin Park', 176), instanciamos a classe musica, criando um objeto.
##Durante a instanciação, o método __init__ é executado e atribui os valores recebidos aos atributos do objeto (self.nome, self.artista, self.duracao).
##Esse objeto criado é então referenciado pela variável n.
##Mesmo tendo os atributos definidos na classe, eles só passam a existir quando a classe é instanciada, criando um objeto que recebe valores para esses atributos.
#
#@dataclass
#class Musica:
#    nome: str
#    artista: str
#    duracao: int
#m = Musica("From The Inside", "Linkin Park", 176)
#print(m)

#O dataclass é uma bliblioteca que ajuda a não ter boilerplate, e deixa CLARO que a classe é um modelo de dados.
# NÃO usar se a classe tem muita lógica, herança pesada e comportamento.

##Classe “normal”
##
##👉 quando o foco é comportamento
##
##@dataclass
##
##👉 quando o foco é dados

#---------#
#class Musica:
#    nome = ''
#    artista = ''
#    duracao = int
#
#musica1 = Musica()
#musica1.nome = 'Bohemian Rhapsody'
#musica1.duracao = 355
#musica1.artista = 'teste'
#
#print(f'Música: {musica1.nome} - Banda: {musica1.artista} - {musica1.duracao} segundos')

#não ira retornar 'missing argument' porque não está sendo passado o método __init__.
#O print funcionará, pois, passando o musica1 = Musica() o objeto nasce sem atributos próprios, e quando acessa musica1.artista, ele "acha" artista na classe e usa '' como padrão.
#-----------------------------------------------#

#Exercicios
#1
#class restaurante:
#    categoria = "Genérica"
#    
#    def __init__(self, nome: str, categoria: str, ativo: bool = False) :
#        self.nome = nome
#        self.categoria = categoria
#        self.ativo = ativo
#
#    def status(self) -> str:
#        return "ativo" if self.ativo else "inativo"
#
#restaurante_praca = restaurante('Praça', 'Brasileira', False)
#
#
#
#
#restaurante_praca.categoria = "Italiana"
#print(vars(restaurante_praca))
#
##2
#print(restaurante_praca.nome)
#
##3
#print(f"O Restaurante está {restaurante_praca.status()}")
#
##4
#categoria = restaurante.categoria
#print("Categoria (classe):",categoria)
#
##5
#restaurante_praca.nome = "Bistro"
#
##6
#restaurante_pizza = restaurante("Pizza Place", "Fast Food")
#
##7
#print(restaurante_pizza.categoria == "Fast Food")
#
##8
#restaurante_pizza.ativo = True
#
##9
#print(f"{restaurante_praca.nome} - {restaurante_praca.categoria}")
#--------------#####################---------------------#
#class Musica:
#    musicas = []
#
#    def __init__(self, nome: str, artista: str, duracao:int):
#        self.nome = nome
#        self.artista = artista
#        self.duracao = duracao
#        Musica.musicas.append(self)
#
#    def __str__(self):
#        return f'{self.nome} | {self.artista} | {self.duracao}'
#    
#    def listar_musicas():
#        for music in Musica.musicas:
#            print(f'{music.nome} | {music.artista} | {music.duracao}')
#
#artista_1 = Musica('Gamesir', 'LG', '180')
#Musica.listar_musicas()
#------Exercícios da Aula-------#

#Exercicio 1
#class Carro:
#    concesionaria = []
#
#    def __init__(self,modelo: str, cor: str, ano:int):
#        self.modelo = modelo
#        self.cor = cor
#        self.ano = ano
#        Carro.concesionaria.append(self)
#
#    def __str__(self):
#        return f'{self.modelo} | {self.cor} | {self.ano}'
#    
#    def listar_carros():
#        for car in Carro.concesionaria:
#            print(f'{car.modelo} | {car.cor} | {car.ano}')
#
#carro1 = Carro('HRV', 'Cinza', 2024)
#Carro.listar_carros()

#Exercicio 2

class Restaurante:
    def __init__(self, nome: str, categoria:str, ativo: bool = False): #__init__ construtor
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo

    def __str__(self): #Foca na visualização
        return f'{self.nome} | {self.categoria} | {self.ativo}'
    
rest = Restaurante('Paris 6', 'Gourmet', True)
print(rest)

# 3) Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros
#    e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.

class Restaurante:
    def __init__(self, nome, categoria, capacidade=0, nota_avaliacao=0.0, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao
        self.ativo = ativo

# Instanciando um restaurante utilizando o construtor
novo_restaurante = Restaurante(nome='Santa Marmita', categoria='Fast Food')



# 4) Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância,
#    seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.

class Restaurante:
    def __init__(self, nome, categoria, capacidade=0, nota_avaliacao=0.0, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao
        self.ativo = ativo

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

# Exibindo uma instância do restaurante formatada
restaurante_formatado = Restaurante(nome='Bom Sabor', categoria='Tradicional')
print(restaurante_formatado)



# 5) Crie uma classe chamada Cliente e pense em 4 atributos.
#    Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class Cliente:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

# Instanciando três objetos da classe Cliente e atribuindo valores aos seus atributos através do construtor
cliente1 = Cliente(nome='Alice', idade=25, email='alice@gmail.com', telefone='123-456-7890')
cliente2 = Cliente(nome='Bob', idade=30, email='bob@gmail.com', telefone='987-654-3210')
cliente3 = Cliente(nome='Charlie', idade=22, email='charlie@gmail.com', telefone='555-123-4567')