from exercicios_oo.exercicios import Livro

livro_biblioteca = Livro("Python in Practice", "Emily Coder", 2021)
print(f"Antes de emprestar (biblioteca): Livro disponível? {livro_biblioteca._disponivel}")
livro_biblioteca.emprestar()
print(f"Depois de emprestar (biblioteca): Livro disponível? {livro_biblioteca._disponivel}")


def main():
    Livro.lista_biblioteca()

if __name__ == '__main__':
    main()