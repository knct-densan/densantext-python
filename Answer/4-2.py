nums = []

for i in range(3):
    n = int(input())
    nums.append(n)

for i in range(3):
    for j in range(i, 3):
        if i == j:
            continue
        if nums[i] == nums[j]:
            print("同じ数字があります。")