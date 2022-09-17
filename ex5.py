store = {
    "Iphone12": 28000000,
    "Samsung N10": 16000000,
    "Oppo 93": 7500000,
    "Vsmart": 7400000,
    "Vivo": 4200000,
}

inp = input("Input name of a phone: ")
try:
    print(f"Price of {inp}: {store[inp]}")
except:
    print("No such phone")
    
    
budget = int(input("Input your budget: "))
print("Phones that fit your budget:")
for key in store:
    if store[key] <= budget:
        print(f"- {key}: {store[key]}")