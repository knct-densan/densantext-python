n = int(input())

# 解答1(for文)
for i in range(1, n + 1):
    # if文を使用する場合
    if i % 4 == 0:
        print(i)

    # continueを使用する場合
    # if i % 4 != 0:
    #     continue
    # print(i)

# 解答2(while文)
# i = 1
# while i <= n:
#     if i % 4 == 0:
#         print(i)
#     i += 1
