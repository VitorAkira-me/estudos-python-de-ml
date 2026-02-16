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

class Restaurante:
    restaurantes = []
    
    def __init__(self, nome: str, categoria: str, ativo: bool = False): #Métodos especiais ->  também conhecidos como "dunder methods" (métodos com duplo sublinhado)
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        Restaurante.restaurantes.append(self)

    def __str__(self): #Utilizado para deixar legivel e visual o retorno
        return f'{self.nome} | {self.categoria} | {self.ativo}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

    def status(self) -> str:
        return "ativo" if self.ativo else "inativo"

restaurante_praca = Restaurante('Praça', 'Gourmet', False)
restaurante_pizza = Restaurante('Pizza Expressa', 'Italiana', True)

Restaurante.listar_restaurantes()