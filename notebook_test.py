# Linguagem: Python
def calcular_media(valores):
    """Calcula a média de uma lista de números, ignorando valores None."""
    filtrados = [x for x in valores if x is not None]
    if len(filtrados) == 0:
        return None  # Evita divisão por zero se lista vazia após filtrar
    return sum(filtrados) / len(filtrados)
# Exemplo de uso da função:
dados = [10, None, 25, 40]
media = calcular_media(dados)
print(f"Média calculada: {media:.2f}" if media is not None else "Lista vazia após filtragem.")