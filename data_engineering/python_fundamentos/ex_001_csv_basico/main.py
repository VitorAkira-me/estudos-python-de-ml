import csv


rows_ok = []
invalid_count = 0
total_count = 0

invalid_reasons = { 
    "missing_quantity": 0,
    "missing_preco": 0,
    "cliente_invalido": 0
}


with open('data_engineering/python_fundamentos/ex_001_csv_basico/data/vendas.csv', mode='r') as file:
    csvFile = csv.DictReader(file)

    for line in csvFile:
        total_count += 1
        is_invalid = False
        try:
            line['quantidade'] = int(line['quantidade'])
        except (ValueError, TypeError):
            line['quantidade'] = None
        try:
            line['preco'] = float(line['preco'])
        except (ValueError, TypeError):
            line['preco'] = None

        cliente = (line.get("cliente") or "").strip()

        if line["quantidade"] is None:
            invalid_reasons["missing_quantity"] += 1
            is_invalid = True

        if cliente == "" or cliente == "-":
            invalid_reasons["cliente_invalido"] += 1
            is_invalid = True
            
        if line["preco"] is None:
            invalid_reasons["missing_preco"] += 1
            is_invalid = True
        
        if is_invalid:
            invalid_count += 1
        else:
            line["cliente"] = cliente.lower()
            rows_ok.append(line)
    assert total_count == len(rows_ok) + invalid_count



print("Linhas válidas:", rows_ok)
print("---------------------")
print("Linhas inválidas:", invalid_count)
print("---------------------")
print("Total de linhas no arquivo:", total_count)
print("---------------------")
print("Razões de invalidação:", invalid_reasons)

# O código acima lê um arquivo CSV chamado 'vendas.csv' localizado no diretório especificado


#print("Linhas:", len(rows))
#print("Primeira:", rows[0])
#print("Ultima:", rows[-1])
#print(rows[0]["produto"])
#print("-----------")
#print(rows)
