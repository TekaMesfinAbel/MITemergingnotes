#----first example---

# what will change in



# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     Wb="Welcome aboard"
#     print(Wb)
    
    
# greet("Abel", "Teka")

# def get_greeting(name):
#     return f"HI {name}"


# message = get_greeting("Abel")
# print(message)

# def increment(number,by=1):
#     return number + by

# print(increment(3,4))

def multiply(*numbers):
    total=1
    for number in numbers:
        total *= number
    return total


print(multiply(1,2,3,4,5,6))