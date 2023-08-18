i,r,k = map(int, input().split(' '))
count = 0
if i < r:
    for j in range(i, r + 1, k):
        count += 1
print(count)