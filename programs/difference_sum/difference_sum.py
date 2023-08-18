test = int(input())
while test:
    N,M = map(int, input().split(' '))
    stt = input().split()
    arr = [int(x) for x in stt]
    arr.sort()
    sub = N - M
    print(sum(arr[-sub:]) - sum(arr[:sub])) 
    test -= 1