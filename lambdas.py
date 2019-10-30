sum = lambda a,b : a + b

print("suma: "+ str(sum(1,2)))


# Map lambdas
names = ["Christian", "yamile", "Anddy", "Lucero", "Evelyn"]
names = map(lambda name:name.upper(),names)
print(list(names))


def decrement_list (*vargs):
    return list(map(lambda number: number - 1,vargs))


print(decrement_list(1,2,3))


#all
def is_all_strings(lst):
    return all(type(l) == str for l in lst)


print(is_all_strings(['2',3]))


#sorted
numbers = [2,3,5,1,8,3,7,9,4]
print(numbers)
print(sorted(numbers))
print(sorted(numbers,reverse=True))
print(numbers)


def extremes(ass):
    return  min (ass),max(ass)

print(extremes([1,2,3,4,5]))
print(extremes("alcatraz"))
print(extremes([1,2,3,4,5]))