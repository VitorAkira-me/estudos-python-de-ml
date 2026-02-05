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

class restaurante:
    categoria = "Genérica"
    
    def __init__(self, nome: str, categoria: str, ativo: bool = False) :
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo

    def status(self) -> str:
        return "ativo" if self.ativo else "inativo"

restaurante_praca = restaurante('Praça', 'Brasileira', False)

#1
restaurante_praca.categoria = "Italiana"
print(vars(restaurante_praca))

#2
print(restaurante_praca.nome)

#3
print(f"O Restaurante está {restaurante_praca.status()}")

#4
categoria = restaurante.categoria
print("Categoria (classe):",categoria)

#5
restaurante_praca.nome = "Bistro"

#6
restaurante_pizza = restaurante("Pizza Place", "Fast Food")

#7
print(restaurante_pizza.categoria == "Fast Food")

#8
restaurante_pizza.ativo = True

#9
print(f"{restaurante_praca.nome} - {restaurante_praca.categoria}")
