# if conditional
hasGoodCredit = True
price = 1000000
if hasGoodCredit:
    print(price * 0.1)
else:
    print(price * 0.2)

hasHighIncome = False
hasGoodCredit = True

if hasGoodCredit and hasHighIncome:
    print("Elegible for loan")
else:
    print("Not Elegible for loan")
