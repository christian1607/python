sum = lambda a,b : a + b

print("suma: "+ str(sum(1,2)))


# Map lambdas
names = ["Christian", "yamile", "Anddy", "Lucero", "Evelyn"]
names = map(lambda name:name.upper(),names)
print(list(names))


def decrement_list (*vargs):
    return list(map(lambda number: number - 1,vargs))


print(decrement_list(1,2,3))