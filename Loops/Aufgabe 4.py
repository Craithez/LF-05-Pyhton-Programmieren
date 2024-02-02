def ggT(x, y):
    while x > 0 and y > 0:
        if x >= y:
            x = x - y
        else:
            y = y - x
    return y

x = int(input("Bitte erste Zahl eingeben: "))
y = int(input("bitte zweite Zahl eingeben: "))       
n = ggT(x,y)
print(n)
