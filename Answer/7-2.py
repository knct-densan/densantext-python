def gcd(x, y):
    if (x < y):
        x, y = y, x
    r = x % y
    if r == 0:
        return y
    else:
        return gcd(y, r)

x = int(input("x = "))
y = int(input("y = "))
print(gcd(x, y))
