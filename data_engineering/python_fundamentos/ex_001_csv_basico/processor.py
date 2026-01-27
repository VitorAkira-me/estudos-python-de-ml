import csv
from pyexpat import errors

def parse_int(value: str) -> int | None:
    '''
    Função para converter uma string em inteiro, se não conseguir, retorna None.
    '''
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

def parse_float(value: str) -> float | None:
    '''
    Função para converter uma string em float, se não conseguir, retorna None.
    '''
    try:
        return float(value)
    except (ValueError, TypeError):
        return None
    
def validate_row(row: dict[str, object]) -> list[str]:
    '''
    Função valida uma linha do CSV como Strings e objects, para então devolver uma lista de strings com os motivos de invalidação.
    
    Output:
    - Lista de strings com os motivos de invalidação.
    '''
    invalid_reasons = []

    if row['cliente'] is None or row['cliente'].strip() == "" or row['cliente'].strip() == "-":
        invalid_reasons.append("cliente_invalido")

    if row['quantidade'] is None or row['quantidade'] <= 0:
        invalid_reasons.append("missing_quantity")

    if row['preco'] is None or row['preco'] < 0:
        invalid_reasons.append("missing_preco")

    return invalid_reasons

def process_rows(rows: list[dict[str, str]]) -> tuple[list[dict], list[dict], dict[str, int]]:
    '''
    Função pestá validando as linhas do CSV e separando se essas linhas são válidas ou inválidas, mostrando também os motivos de invalidação e a contagem de cada motivo.
    
    Output:
    - Tupla com:
        - Lista de linhas válidas.
        - Lista de linhas inválidas.
        - Dicionário com a contagem de motivos de invalidação.
    '''
    valid_rows = []
    invalid_rows = []
    reasons_count = {
        "missing_quantity": 0,
        "missing_preco": 0,
        "cliente_invalido": 0
    }

    for row in rows:
        row['quantidade'] = parse_int(row.get('quantidade'))
        row['preco'] = parse_float(row.get('preco'))
        errors = validate_row(row)
        
        if not  errors:
            valid_rows.append(row)
        else:
            invalid_rows.append(row)
            for reason in errors:
                reasons_count[reason] += 1
    return valid_rows, invalid_rows, reasons_count

def main():
    '''
    Função main para ler o arquivo CSV, processar as linhas e imprimir os resultados.
    '''
    with open('data_engineering/python_fundamentos/ex_001_csv_basico/data/vendas.csv', mode='r') as file:
        csvFile = csv.DictReader(file)
        rows = list(csvFile)

    valid_rows, invalid_rows, reasons_count = process_rows(rows)

    print("Linhas válidas:", valid_rows)
    print("---------------------")
    print("Linhas inválidas:", len(invalid_rows))
    print("---------------------")
    print("Total de linhas no arquivo:", len(rows))
    print("---------------------")
    print("Razões de invalidação:", reasons_count)

if __name__ == "__main__":
    main()
