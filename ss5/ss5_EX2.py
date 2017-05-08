# Create a new dictionary called prices using {} format like the example above
prices = {
    "banana" : 4,
    "apple" : 2,
    "orange" : 1.5,
    "pear" : 3
}

# And these values in your stock dictionary:
stock = {
    "banana" : 6,
    "apple" : 0,
    "orange" : 1.5,
    "pear" : 15
}

#Loop through each key in prices. For each key, print out the key along with
#its price and stock information. Print the answer in the following format:
#apple
#price: 2

for key in prices:
    print("price: {0}".format(prices[key]))
    print("stock: {0}\n".format(stock[key]))

total = 0


for key in prices:
    money = prices[key] * stock[key]
    print("Money from selling {0}: {1}".format(key, money))
    total = total + money

print ( "\nMoney that I would make if i sold all of my foods: {0}".format(total) )
