def index_differences(arr):
    first_occurrence = {}
    last_occurrence = {}
    sum_abs_index_diff = 0

    for i, num in enumerate(arr):
        if num not in first_occurrence:
            first_occurrence[num] = i
        last_occurrence[num] = i

    for num in set(arr):
        sum_abs_index_diff += abs(last_occurrence[num] - first_occurrence[num])

    return sum_abs_index_diff

t    = int(input())
while t > 0:
    size         = int(input())
    numbers      = input().split(' ')
    array        = [int(i) for i in numbers]
    s            = 0
    i = 0
    s            = index_differences(array)
    print(s)
    t -= 1


# t = int(input())
# while t > 0:
#     t -= 1
#     n = int(input())
#     have = {}
#     a = list(map(int, input().split()))
#     for i in range(n):
#         if a[i] not in have:
#             have[a[i]] = []
#         have[a[i]] += [i]
#     ans = 0
#     for key, occ in have.items():
#         ans += occ[-1] - occ[0]
#     print(ans)
