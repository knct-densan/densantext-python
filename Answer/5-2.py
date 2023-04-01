def init_zero(values):
    n = len(values)
    values.clear()
    values.extend([0] * n)

a = [1, 2, 3, 4]
init_zero(a)
print(a) # [0, 0, 0, 0]
