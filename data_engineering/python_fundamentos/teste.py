#def gerador(n):
#    for i in range(n):
#        yield i
#
#gen = gerador(3)
#valores = [x for x in gen]
#print(valores)

#lista = [1, 2, 3, 4, 5]
#nova_lista = [x * 2 for x in lista if x % 2 == 0]
#print(nova_lista)

#ef foo(x):
#   return x + 1
#
#ef bar(y):
#   return y * 2
#
#alor = 3
#
#esultado = (foo if valor % 2 == 0 else bar)(valor)
#rint(resultado)

#def greet(name, prefix="Mr."):
#    return f"{prefix} {name}"
#
#print(greet("Akira"))
#print(greet("Akira", "Dr."))


from desafio_lambdas_2 import apply_discount, sort_by_price, products

discounted = apply_discount(products, 10)
sorted_products = sort_by_price(discounted)
print(sorted_products)
