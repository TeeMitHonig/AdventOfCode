file = open("./day1-input")
input = file.read().split("\n")
file.close()


value = 50
zeronum = 0

for i in input:
    if i:
        oldvalue = value
        dir = i[0]
        amount = int(i[1:])

        if (dir == "R"):
            value += amount

        if (dir == "L"):
            value -= amount
        value %= 100
        if (value == 0):
            zeronum += 1

        print(f"{oldvalue} --{i}--> {value}")


print(zeronum)
