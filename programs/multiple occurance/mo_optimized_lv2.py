t    = int(input())
while t > 0:
    size         = int(input())
    numbers      = input().split(' ')
    array        = [int(i) for i in numbers]
    array_length = len(array) - 1
    records      = []
    s            = 0
    i = 0
    while i <= array_length:
        j = array_length
        print(records)
        while j > i and array[i] not in records:
            test = array[j] == array[i]
            if test and j == array_length:
                array_length -= 1
            if test:
                records.append(array[i])
                s = s + (j - i)
                break 
            j -= 1 
        i += 1
    print(s) 
    t -= 1