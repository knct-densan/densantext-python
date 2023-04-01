def sum_n(n):
    if (n <= 1):
        return 1
    return n + sum_n(n - 1)

n = int(input())
print(sum_n(n))
