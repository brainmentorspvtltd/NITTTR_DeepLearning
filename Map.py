##def tempConv(c):
##    return 9 / 5 * c + 32

c = [34.5,33.2,37.8,29.8,27.8]

##for temp in c:
##    print(tempConv(temp))

f = list(map(lambda cel : 9 / 5 * cel + 32, c))
print(f)
