def stats(*numeros):
    """
    Recebe vários números e retorna um dicionário com:
    - quantidade
    - soma
    - média
    - maior
    - menor
    """
    len_nums = len(numeros)
    numbs = 0

    if not numeros:
        return None


    for num in numeros:
        numbs += num
        media = numbs / (len_nums)
        max_n = max(numeros)
        min_n = min(numeros)
    return {
            'count' : len_nums,
            'sum' : numbs,
            'mean' : media,
            'max' : max_n,
            'min' : min_n
        }

def describe_user(**info):
    """
    Se tiver nome, idade e cidade, imprime assim:
    "Akira (23) - São Paulo"

    Se faltar algo, usa um valor padrão tipo "N/A".
    """
    nome = info.get("nome", "N/A")
    idade = info.get("idade", "N/A")
    cidade = info.get("cidade", "N/A")
    print(f"{nome} ({idade}) - {cidade}")