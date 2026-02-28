#Quando pensamos em classe, pensamos nas caracteristicas, os atributos que da entidade que estamos criando.
#Ex: Classe de pessoa = nome, idade, peso, etc.
# Uma classe no python, pode ter funções, atributos e métodos.

#class restaurante:
#    nome = '' #atributos
#    categoria = '' #atributos
#    ativo = False #atributos
#
#restaurante_praca = restaurante()
#restaurante_praca.nome = 'Praça'
#restaurante_praca.categoria = 'Gourmet'
#
#restaurante_pizza = restaurante()
#
#restaurantes = [restaurante_praca, restaurante_pizza]
##[<__main__.restaurante object at 0x000001E941165C40>, <__main__.restaurante object at 0x000001E941165C70>]
## o codigo acima nao esta mostrando as informações, so esta mostrando aonde esta sendo armazenado
#print(vars(restaurante_praca))
#---------------------MEU JEITO------------------------#
#Tipo | Atua sobre
#self | objeto
#cls  | classe inteira

#| Pergunta                    | Resposta            |
#| --------------------------- | ------------------- |
#| pertence a um restaurante?  | método de instância |
#| pertence ao sistema todo?   | classmethod         |
#| só muda a forma de mostrar? | property            |
#| cria o objeto?              | **init**            |


from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria): #Métodos especiais ->  também conhecidos como "dunder methods" (métodos com duplo sublinhado)
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self): #Utilizado para deixar legivel e visual o retorno
        return f'{self._nome} | {self._categoria} | {self.ativo}'
    
    @classmethod #Utilizando informações a esse método, trabalha com a classe INTEIRA não com 1 restaurante apenas.
    #→ método de classe (cls)
    def listar_restaurantes(cls):
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}")
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}")

    @property #capacidade de pegar um atributo = Ativo, modificar como aquele atributo vai ser lido #Podemos utilizar para operação matematica e para realizar como pegar valores e agrupar em um valor. 
    #O _ antes do atributo deixa "protegido" onde aquele atribuito não é para ser modificado.
    #→ leitura controlada do atributo
    def ativo(self):
        return '✕' if self._ativo else '▢'

    def alternar_estado(self): # → método de instância (self)
        self._ativo = not self._ativo #invester de True -> False vise-versa

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media