def format_user(name, age, city):
    user = {
        'name' : name,
        'age' : int(age),
        'city' : city
        }
    return user


user = format_user("Akira", 23, "São Paulo")
print(user)
