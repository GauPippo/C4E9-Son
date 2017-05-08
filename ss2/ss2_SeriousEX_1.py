shop = ["T-Shirt","Sweater"]

n = input("Welcome to our shop, what do you want(C,R,U,D)?:")
if n == "C":
    m = input("Enter new items:")
    shop.append(m)
    print("Our items:", shop)

elif n == "R":
    print("Our items:", shop)
    
elif n == "U":
    up = int(input("Update position?"))
    ni = input("New items?")
    shop.insert(up, ni) 
    print("Our items", shop)

elif n == "D":
    delete = int(input("Delete position?"))
    shop.pop(delete)
    print("Our items:", shop)
else:
    print("Syntax Erros...")

