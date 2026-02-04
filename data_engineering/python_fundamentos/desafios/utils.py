#def format_user(name, age, city):
#    return {
#        "name" : name,
#        "age" : int(age),
#        "city" : city
#    }
#
#def sum(a, b):
#    return a + b
#
#def welcome(name):
#    return f"Bem-vindo, {name}!"

#def format_user(name, age, city):
#    return {
#        "name" : name,
#        "age" : int(age),
#        "city" : city.capitalize()
#    }
#
#def math_operations(a,b):
#        #numbers = [a,b]
#        return {
#        "input_a" : a,
#        "input_b" : b,
#        "sum" : a + b,
#        "product" : a * b,
#        "average" : (a + b) / 2
#        }
#
#def welcome_message(name):
#    return f"Welcome back, {name}! Ready to code?"



def filter_even(numbers):
    evens = []
    for n in numbers:
        if n % 2 == 0:
            evens.append(n)
    return evens

def safe_divide(a,b):
    try:
        if a <= 0 or b <= 0:
            return "Inválido. Digite um número maior que 0"
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid types"