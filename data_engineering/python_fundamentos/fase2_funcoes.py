from stats_utils import stats, describe_user

#resultado = stats(10, 5, 2, 8)
#print(resultado)
#
#describe_user(nome="Akira", idade=23, cidade="São Paulo")
#describe_user(nome="Maria")


#def stats_lista(numeros):
#    """
#    Recebe uma lista de números e usa stats(*numeros)
#    para devolver o mesmo dicionário de estatísticas.
#    """ 
#    return stats(*numeros)
#
#resultado = stats_lista([3, 7, 1, 9])
#print(resultado)
## deve dar o mesmo formato do stats normal
#
#
#def describe_users(lista_de_usuarios):
#    """
#    Recebe uma lista de dicionários, ex:
#    [
#        {"nome": "Akira", "idade": 23, "cidade": "São Paulo"},
#        {"nome": "Maria"},
#        ...
#    ]
#    e chama describe_user(**usuario) para cada um.
#    """
#    for user in lista_de_usuarios:
#        describe_user(**user)
#
#
#usuarios = [
#    {"nome": "Akira", "idade": 23, "cidade": "São Paulo"},
#    {"nome": "Maria"},
#    {"nome": "João", "idade": 19},
#]
#
#describe_users(usuarios)
#
#
#def resumo_treino(nome, *reps, **infos):
#    """
#    nome: nome da pessoa
#    *reps: várias cargas/repetições (números)
#    **infos: dados extras, ex: exercicio="Supino", dia="Segunda"
#    - Imprime o nome
#    - Imprime o exercício (se veio)
#    - Imprime stats das reps usando stats(*reps)
#    """
#    exercicio = infos.get('exercicio', 'N/A')
#    dia = infos.get('dia', 'N/A')
#
#    print(f"{nome} - {exercicio} ({dia})")
#
#    reps_stats = stats(*reps)
#    print(f"Reps stats: {reps_stats}")
#    
#    return reps_stats
#
#resumo_treino(
#    "Akira",
#    10, 12, 8, 15,
#    exercicio="Supino",
#    dia="Segunda"
#)        

#Akira - Supino (Segunda)
#Reps stats: {'count': 4, 'sum': 45, 'mean': 11.25, 'max': 15, 'min': 8}



def workout_stats(*reps):
    """
    Recebe várias reps (números) e devolve:
    - o dicionário de stats (usando stats(*reps))
    - + um campo 'nivel':
        - 'leve' se a média < 8
        - 'moderado' se 8 <= média < 12
        - 'pesado' se média >= 12
    """

    dados = stats(*reps)
    mean = dados['mean']

    if mean < 8:
        nivel = "leve"
    elif 8 <= mean < 12:
        nivel ="moderado"
    elif mean >= 12:
        nivel ="pesado"

    dados["nivel"] = nivel
    return dados

print(workout_stats(6, 8, 10))     # média 8 -> nivel "moderado"
print(workout_stats(12, 15, 14))   # nivel "pesado"
print(workout_stats(5, 6))         # nivel "leve"



def log_workout(nome, *reps, **info_extra):
    """
    nome: nome da pessoa
    *reps: números (cargas, reps, etc)
    **info_extra: exercicio, dia, anotacoes, etc

    A função deve:
    - calcular stats das reps usando workout_stats(*reps)
    - montar um dicionário com:
        {
        'nome': ...,
        'exercicio': ...,
        'dia': ...,
        'stats': {...}
        }
    - usar valores padrão se algo não vier em info_extra
    - retornar esse dicionário
    """

    #name = log_workout(nome)
    #repit = log_workout(*reps)
    #info_ext = log_workout(**info_extra)
    exercicio = info_extra.get('exercicio', 'N/A')
    dia = info_extra.get('dia', 'N/A')

    calc_reps = workout_stats(*reps)


    return {
        'nome': nome,
        'exercicio': exercicio,
        'dia': dia,
        'stats': calc_reps
        
    }


treino1 = log_workout("Akira", 10, 12, 8, 15, exercicio="Supino", dia="Segunda")
treino2 = log_workout("Maria", 6, 6, 7, exercicio="Agachamento")

print(f"Meu treino 1: {treino1}")
print(f"Meu treino 2: {treino2}")


treinos = [
    log_workout("Akira", 10, 12, 8, 15, exercicio="Supino", dia="Segunda"),
    log_workout("Maria", 6, 6, 7, exercicio="Agachamento", dia="Terça"),
    log_workout("João", 14, 13, 15, exercicio="Terra", dia="Quarta"),
]

treino_pesado = [t for t in treinos if t["stats"]["nivel"] == 'pesado']
print(f"Treino: {treino_pesado}")


supino_treinos = list(filter(lambda t: t["exercicio"] == "Supino", treinos))
nomes_supino = [t["nome"] for t in supino_treinos]
print(nomes_supino)   # deve aparecer ["Akira"]
