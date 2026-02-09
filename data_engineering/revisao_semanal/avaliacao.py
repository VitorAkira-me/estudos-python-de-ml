#Revisão de de segunda feira

#nome = input("Qual o nome do aluno: ")
#nota = float(input("Coloque uma nota: "))
#faltas = int(input("Quantas vezes faltou: "))
#
#if nota >= 6 and nota <= 10 and faltas <=10:
#    print("Aluno aprovado")
#elif nota < 6 and faltas >= 11 and faltas < 15:
#    print("Recuperação")
#elif nota > 10 or nota < 0:
#    print("Nota inválida")
#else:
#    print("Aluno REPROVADO")
#    
#------------------------#####------------------#

#class musica:
#    def __init__(self, nome: str, artista: str, duracao: int):
#        self.nome = nome
#        self.artista = artista
#        self.duracao = duracao
#
#n = musica('From The Inside', 'Linkin Park', 176)
#print(vars(n))

class Musica:
    nome = ''
    artista = 'oi'
    duracao = int

musica1 = Musica()
musica1.nome = 'Bohemian Rhapsody'
musica1.duracao = 355
print(vars(Musica))
#print(f'Música: {musica1.nome} - Banda: {musica1.artista} - {musica1.duracao} segundos')
