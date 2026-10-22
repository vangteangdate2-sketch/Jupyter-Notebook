prices = [25,120,45,300,80,150,20,250]

# a) find product above 100
above = list(filter(lambda x: x >= 100, prices))
print("Above 100 are", above)

# b) find product between 50 and 200, inclusive
inclusive = list(filter(lambda x: 50 <= x <= 200 , prices))
print("Price between 50 and 200 are", inclusive)

# c) apply a 10% discount to every price 
discount = list(map(lambda x: x * 0.90, prices))
print("10% discount are", discount)

# d) sort discounted prices from highest to lowest
sort = sorted(discount)
print("Sorted Discount are", sort)

# e) calculate the avg price 
avg_price = sum(prices) / len(prices)
print("Average Price are", avg_price)