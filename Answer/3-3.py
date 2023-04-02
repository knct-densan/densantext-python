n = int(input())

# 解答1
for i in range(0, n):
    for j in range(0, i + 1):
        print('*', end='')
    print()

# 解答2
# こちらの方がPythonらしく、簡潔に書けます。
# for i in range(1, n + 1):
#     print('*' * i)