import csv


rows_ok = []
invalid_count = 0

with open('data_engineering/python_fundamentos/ex_001_csv_basico/data/vendas.csv', mode='r') as file:
    csvFile = csv.DictReader(file)

    for line in csvFile:
        try:
            line['quantidade'] = int(line['quantidade'])
        except (ValueError, TypeError):
            line['quantidade'] = None

        try:
            line['preco'] = float(line['preco'])
        except (ValueError, TypeError):
            line['preco'] = None
        
        if line["quantidade"] is None:
            invalid_count += 1
        elif line["preco"] is None:
            invalid_count += 1
        else:
            line["cliente"] = line["cliente"].strip().lower()
            rows_ok.append(line)

        

print("Linhas válidas:", rows_ok)
print("Linhas inválidas:", invalid_count)

# O código acima lê um arquivo CSV chamado 'vendas.csv' localizado no diretório especificado


#print("Linhas:", len(rows))
#print("Primeira:", rows[0])
#print("Ultima:", rows[-1])
#print(rows[0]["produto"])
#print("-----------")
#print(rows)
