#def even(num):
#    return num % 2 == 0

# print(even(12))

numbers = [i for i in range(51)]

#for n in numbers:
#    print(even(n))

#e = list(filter(even, numbers))
#print(e)

e = list(filter(lambda x : x % 2 == 0, numbers))
print(e)
