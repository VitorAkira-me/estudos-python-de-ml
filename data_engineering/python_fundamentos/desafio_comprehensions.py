from utils import filter_even, safe_divide

#Challenge 1
numbers = [1,2,3,4,5,6,7,8]

#even_numbers = [n for n in numbers if n % 2 == 0]
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
print("Even:", even_numbers)

#squared_odds = [n ** 2 for n in numbers if n % 2 != 0]
squared_odds = list(map(lambda n: n ** 2, 
                        filter(lambda n : n % 2 != 0, numbers)))
print("Squared odds:", squared_odds)

bigger_10 = [1,20,3,4,5,68,7,81,9,10]
#bigger_than_10 = [i * 3 for i in numbers if i *3 > 10]
bigger_than_10 = list(map(lambda n: n *3, 
                        filter(lambda n: n > 10, bigger_10)))
print("Bigger than 10:", bigger_than_10)

##Challenge 2
users = [
    {"name": "Akira", "age": 23, "city": "São Paulo"},
    {"name": "Maria", "age": 30, "city": "Rio de Janeiro"},
    {"name": "João", "age": 19, "city": "São Paulo"},
    {"name": "Ana", "age": 40, "city": "Curitiba"},
]

user_sorted_by_age = sorted(users, key=lambda u: u["age"])

names_upper = list(map(lambda n: n["name"].upper(), users))
print(names_upper)

names = [u["name"] for u in users]
ages = [u["age"] for u in users]
age_by_name = dict(zip(names, ages))
print(age_by_name)

for index, dict_items in enumerate(users, start=1):
    print(f"#: {index} - {dict_items['name']} ({dict_items['age']}) - {dict_items['city']} ")


#adult_users = [user for user in users if user['age'] >= 21]
#print("Adult users:", adult_users)
#
#names_from_sp = [name['name'] for name in users if name['city'] == 'São Paulo']
#print("Names from SP:", names_from_sp)
#
#age_by_name = {user['name'] : user['age'] for user in users}
#print("Age by name:", age_by_name)

##Challennge 3
#
#pairs = [(10, 2), (5, 0), (8, 4), ("10", 2), (20, -1)]
#results = []
#
#for a,b in pairs:
#    divide = safe_divide(a,b)
#    results.append(divide)
#print(results)
