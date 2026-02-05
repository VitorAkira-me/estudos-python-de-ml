import csv
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database.db"

def parse_int(value: str):
    value = (value or "").strip()
    return int(value) if value else None

def parse_float(value: str):
    value = (value or "").strip().replace(",", ".")
    return float(value) if value else None


CONFIG = [
    # CLIENTES
    {
        "table": "clientes",
        "csv": BASE_DIR / "data" / "tabela_clientes_desafio_aula_1.csv",
        "create_sql": """
            CREATE TABLE IF NOT EXISTS clientes (
                id_cliente INTEGER PRIMARY KEY,
                nome_do_cliente TEXT,
                data_de_cadastro TEXT
            );
        """,
        "columns": ["id_cliente", "nome_do_cliente", "data_de_cadastro"],
        "csv_headers": ["id_cliente", "nome_do_cliente", "data_de_cadastro"],
        "row_map": lambda r: (
            parse_int(r["id_cliente"]),
            r["nome_do_cliente"],
            r["data_de_cadastro"],
        ),
    },

    # PRODUTOS
    {
        "table": "produtos",
        "csv": BASE_DIR / "data" / "tabela_produtos_desafio_aula_1.csv",
        "create_sql": """
            CREATE TABLE IF NOT EXISTS produtos (
                id_produto INTEGER PRIMARY KEY,
                nome_do_produto TEXT,
                preco_unitario REAL
            );
        """,
        "columns": ["id_produto", "nome_do_produto", "preco_unitario"],
        "csv_headers": ["id_produto", "nome_do_produto", "preco_unitario"],
        "row_map": lambda r: (
            parse_int(r["id_produto"]),
            r["nome_do_produto"],
            parse_float(r["preco_unitario"]),
        ),
    },

    # VENDAS
    {
        "table": "vendas",
        "csv": BASE_DIR / "data" / "tabela_vendas_desafio_aula_1.csv",
        "create_sql": """
            CREATE TABLE IF NOT EXISTS vendas (
                id_venda INTEGER PRIMARY KEY,
                id_cliente INTEGER,
                id_produto INTEGER,
                quantidade_comprada INTEGER,
                data_da_venda TEXT,
                FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
                FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
            );
        """,
        "columns": ["id_venda", "id_cliente", "id_produto", "quantidade_comprada", "data_da_venda"],
        "csv_headers": ["id_venda", "id_cliente", "id_produto", "quantidade_comprada", "data_da_venda"],
        "row_map": lambda r: (
            parse_int(r["id_venda"]),
            parse_int(r["id_cliente"]),
            parse_int(r["id_produto"]),
            parse_int(r["quantidade_comprada"]),
            r["data_da_venda"],
        ),
    },
]



def validate_headers(reader: csv.DictReader, expected: list[str], table: str) -> None:
    got = reader.fieldnames or []
    if got != expected:
        raise ValueError(
            f"Cabeçalho do CSV não bate para '{table}'.\n"
            f"Esperado: {expected}\n"
            f"Recebido: {got}"
        )


def import_table(conn: sqlite3.Connection, cfg: dict) -> int:
    cur = conn.cursor()
    cur.execute(cfg["create_sql"])

    # reimport do zero (opcional)
    cur.execute(f"DELETE FROM {cfg['table']};")

    with open(cfg["csv"], mode="r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        validate_headers(reader, cfg["csv_headers"], cfg["table"])
        rows = [cfg["row_map"](r) for r in reader]

    placeholders = ", ".join(["?"] * len(cfg["columns"]))
    cols = ", ".join(cfg["columns"])

    cur.executemany(
        f"INSERT INTO {cfg['table']} ({cols}) VALUES ({placeholders});",
        rows,
    )
    conn.commit()
    return len(rows)



def main() -> None:
    conn = sqlite3.connect(DB_PATH)

    for cfg in CONFIG:
        total = import_table(conn, cfg)
        print(f"Import OK ✅ {cfg['table']}: total de linhas = {total}")

    conn.close()


if __name__ == "__main__":
    main()
