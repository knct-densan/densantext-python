a = []
b = []

for i in range(3):
    n = int(input())
    a.append(n)
for i in range(3):
    n = int(input())
    b.append(n)

for i in range(3):
    a[i], b[i] = b[i], a[i]

print(a)
print(b)
