def comp(x, y):
    if x > y:
        return 1
    elif x < y:
        return -1
    else:
        return 0

print(comp(1, 0)) # 1
print(comp(0, 1)) # -1
print(comp(0, 0)) # 0
