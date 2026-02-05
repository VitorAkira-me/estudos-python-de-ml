from dataclasses import dataclass

class musica:
    def __init__(self, nome: str, artista: str, duracao: int):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

n = musica('From The Inside', 'Linkin Park', 176)
print(vars(n))
#Ao instanciar a classe musica, um objeto é criado e o método __init__ atribui valores aos seus atributos.
#Ao chamar musica('From The Inside', 'Linkin Park', 176), instanciamos a classe musica, criando um objeto.
#Durante a instanciação, o método __init__ é executado e atribui os valores recebidos aos atributos do objeto (self.nome, self.artista, self.duracao).
#Esse objeto criado é então referenciado pela variável n.
#Mesmo tendo os atributos definidos na classe, eles só passam a existir quando a classe é instanciada, criando um objeto que recebe valores para esses atributos.

@dataclass
class Musica:
    nome: str
    artista: str
    duracao: int
m = Musica("From The Inside", "Linkin Park", 176)
print(m)

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
class Musica:
    nome = ''
    artista = ''
    duracao = int

musica1 = Musica()
musica1.nome = 'Bohemian Rhapsody'
musica1.duracao = 355

print(f'Música: {musica1.nome} - Banda: {musica1.artista} - {musica1.duracao} segundos')

#não ira retornar 'missing argument' porque não está sendo passado o método __init__.
#O print funcionará, pois, passando o musica1 = Musica() o objeto nasce sem atributos próprios, e quando acessa musica1.artista, ele "acha" artista na classe e usa '' como padrão.
#-----------------------------------------------#

#Exercicios
