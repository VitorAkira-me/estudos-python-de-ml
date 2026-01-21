from utils import format_user, math_operations, welcome_message
#from utils import format_user, sum, welcome
#import utils as u

#user = format_user("Akira", 23, "São Paulo")
#print(user)
#
#print( sum(10,5))
#print( welcome("Akira"))
#
#print(u.sum(3,4))
#print(u.format_user("João", 30, "Santos"))

user1 = format_user("Akira", 23, "são paulo")
user2 = format_user("joão", 30, "Santos")
print(f"User 1: {user1}")
print(f"User 2: {user2}")

math = math_operations(10,5)
print(f"Math results {math['input_a']} and {math['input_b']}: ")
#for key, value in dict_math.items():
print(f"Sum: {math['sum']} \nProduct: {math['product']} \nAverage: {math['average']}")

#for key, value in user1.items():
print(welcome_message(user1['name']))
print(welcome_message(user2['name']))
    #break
