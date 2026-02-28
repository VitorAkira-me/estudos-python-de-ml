from dataclasses import dataclass
from decimal import Decimal
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

#class Restaurante:
#    def __init__(self, nome: str, categoria:str, ativo: bool = False): #__init__ construtor
#        self.nome = nome
#        self.categoria = categoria
#        self.ativo = ativo
#
#    def __str__(self): #Foca na visualização
#        return f'{self.nome} | {self.categoria} | {self.ativo}'
#    
#rest = Restaurante('Paris 6', 'Gourmet', True)
#print(rest)
#
## 3) Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros
##    e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
#
#class Restaurante:
#    def __init__(self, nome, categoria, capacidade=0, nota_avaliacao=0.0, ativo=False):
#        self.nome = nome
#        self.categoria = categoria
#        self.capacidade = capacidade
#        self.nota_avaliacao = nota_avaliacao
#        self.ativo = ativo
#
## Instanciando um restaurante utilizando o construtor
#novo_restaurante = Restaurante(nome='Santa Marmita', categoria='Fast Food')
#
#
#
## 4) Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância,
##    seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
#
#class Restaurante:
#    def __init__(self, nome, categoria, capacidade=0, nota_avaliacao=0.0, ativo=False):
#        self.nome = nome
#        self.categoria = categoria
#        self.capacidade = capacidade
#        self.nota_avaliacao = nota_avaliacao
#        self.ativo = ativo
#
#    def __str__(self):
#        return f'{self.nome} | {self.categoria}'
#
## Exibindo uma instância do restaurante formatada
#restaurante_formatado = Restaurante(nome='Bom Sabor', categoria='Tradicional')
#print(restaurante_formatado)
#
#
#
## 5) Crie uma classe chamada Cliente e pense em 4 atributos.
##    Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
#
#class Cliente:
#    def __init__(self, nome, idade, email, telefone):
#        self.nome = nome
#        self.idade = idade
#        self.email = email
#        self.telefone = telefone
#
## Instanciando três objetos da classe Cliente e atribuindo valores aos seus atributos através do construtor
#cliente1 = Cliente(nome='Alice', idade=25, email='alice@gmail.com', telefone='123-456-7890')
#cliente2 = Cliente(nome='Bob', idade=30, email='bob@gmail.com', telefone='987-654-3210')
#cliente3 = Cliente(nome='Charlie', idade=22, email='charlie@gmail.com', telefone='555-123-4567')

#-------------------------------------################------------------------------------------#
#Desafio 03.
#Agora é sua vez! Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. 
#Adicione um método especial __str__ para imprimir uma representação em string da pessoa. 
#Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. 
#Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.

#class Pessoa:
#
#    def __init__(self, nome, idade, profissao):
#        self.nome = nome
#        self.idade = int(idade)
#        self.profissao = profissao
#
#    def __str__(self):
#        return f'{self.nome} | {self.idade} | {self.profissao}'
#
#    def __repr__(self):
#        return f"Pessoa(nome='{self.nome}', idade={self.idade}, profissao='{self.profissao}')"
#
#    def aniversario(self):
#        self.idade += 1
#
#    @property
#    def saudacao(self):
#        return f'Olá {self.nome}, que legal que você trabalha com {self.profissao}!'
#
#pessoa_1 = Pessoa('Akira', 24, 'Dados')
#pessoa_1.aniversario()
#print(pessoa_1.saudacao)
#print(pessoa_1)

#--------
#Exercicio Hora da prática do módulo 03.Property e métodos de classe

#class ContaBancaria:
#    def __init__(self,titular, saldo):
#        self._titular = titular
#        self._saldo = saldo
#        self._ativo = False
#
#    def __str__(self):
#        return f'{self._titular} | {self._saldo:.3f} | {self.ativo}'
#    
#    @property
#    def ativo(self):
#        # Retorna o texto baseado no valor booleano
#        return "Ativado" if self._ativo else "Desativado"
#
#    def ativar_conta(self):
#        # O 'not' inverte o valor atual: se era False, vira True
#        self._ativo = not self._ativo
#
#usuario_1 = ContaBancaria('Marcia', 4.500)
#usuario_1.ativar_conta()
#usuario_2 = ContaBancaria('Jorge', 2.800)
#print(usuario_1)
#print(usuario_2)
#
#class ContaBancariaPythonica:
#    def __init__(self, titular, saldo):
#        self._titular = titular
#        self._saldo = saldo
#        self._ativo = False
#
#    @property
#    def titular(self):
#        return self._titular
#
#    @property
#    def saldo(self):
#        return self._saldo
#
#    @property
#    def ativo(self):
#        return self._ativo
#    
#    def ativar_conta(self):
#        self._ativo = True
#
#conta4 = ContaBancariaPythonica("Fernanda", 1500)
#print(f"Titular da conta 4: {conta4.titular}")
#
## 6) Crie uma classe chamada `ClienteBanco` com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
#class ClienteBanco:
#    def __init__(self, nome, idade, endereco, cpf, profissao):
#        self.nome = nome
#        self.idade = idade
#        self.endereco = endereco
#        self.cpf = cpf
#        self.profissao = profissao
#
#cliente1 = ClienteBanco("Ana", 30, "Rua A", "123.456.789-01", "Backend")
#cliente2 = ClienteBanco("Luiza", 25, "Rua B", "987.654.321-01", "Estudante")
#cliente3 = ClienteBanco("Vinny Neves", 40, "Rua C", "111.222.333-44", "Frontend")
#
## 7) Crie um método de classe para a conta `ClienteBanco`.
#class ClienteBanco:
#    # ... (outros métodos e atributos)
#
#    @classmethod
#    def criar_conta(cls, titular, saldo_inicial):
#        conta = ContaBancariaPythonica(titular, saldo_inicial)
#        return conta
#
## Exemplo de uso do método de classe
#conta_cliente1 = ClienteBanco.criar_conta("Ana", 2000)
#print(f"Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}")

#-----------------###################--------------------------#

class Livro:
    biblioteca = []
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.biblioteca.append(self)

    def __str__(self):
        return f"Titulo do livro: {self._titulo} | Autor: {self._autor} | Ano publicado: {self._ano_publicacao} | Disponibilidade: {self.ativado}"

    @classmethod
    def lista_biblioteca(cls):
        print(f"{'Titulo'.ljust(25)} | {'Autores'.ljust(25)} | {'Ano de publicação'.ljust(25)} | {'Disponibilidade'}")
        for bibliotec in cls.biblioteca:
            print(f"{bibliotec._titulo.ljust(25)} | {bibliotec._autor.ljust(25)} | {str(bibliotec._ano_publicacao).ljust(25)} | {bibliotec.ativado}")

    @property
    def ativado(self):
        return 'Disponivel' if self._disponivel else 'Indisponivel'

    def emprestar(self):
        self._disponivel = not self._disponivel

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis




