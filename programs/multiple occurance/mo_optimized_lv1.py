t    = int(input())
while t > 0:
    size         = int(input())
    numbers      = input().split(' ')
    array        = [int(i) for i in numbers]
    array_length = len(array)
    array_       = array_length - 1
    s            = 0
    for i in range(0, array_):
       
        max_j = i
        if array[i] == 0:
            continue
        for j in range(i+1, array_length):
            if array[j] == array[i]:
                array[j] = 0
                max_j    = j
        array[i] = 0
        s = s + (max_j - i)
    print(s) 
    t -= 1