l = [5, 7, 300, 90, 24, 90, 75]

print("Hello, my name is Hiep and these are my ship sizes\n", l)
print("-------------------------------------------\n")

# Month 1
list_1 = [x + 50 for x in l]
print("Month 1\nOne month has passed, now here is my flock\n",list_1)
n = max(list_1)
print("Now my biggest sheep has size", n, "let's shear it")

for m,i in enumerate(list_1):
    if i == n:
        list_1[m] = 8
print("After shearing, here is my flock\n", list_1)
print("------------------------------------------\n")

# Month 2
list_2 = [x + 50 for x in list_1]
print("Month 2\nTwo month has passed, now here is my flock\n", list_2)
n = max(list_2)
print("Now my biggest sheep has size", n, "let's shear it")

for m,i in enumerate(list_2):
    if i == n:
        list_2[m] = 8
print("After shearing, here is my flock\n", list_2)
print("-------------------------------------------\n")

# Month 3
list_3 = [x + 50 for x in list_2]
print("Month 3\nThree month has passed, now here is my flock\n", list_3)
n = max(list_3)
print("Now my biggest sheep has size", n, "let's shear it")

for m,i in enumerate(list_3):
    if i == n:
        list_3[m] = 8
print("After shearing, here is my flock\n", list_3)
print("-------------------------------------------")

# Tính Tiên`
total = 0
for i in list_3:
    total = total + i
print("My flock has size in total:", total)
total = total * 2
print("I would get:", total, "$")

