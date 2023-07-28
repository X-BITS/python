# version : python 3.9   
# desc    : Determine the minimum number of operations to delete the entire array by deleting a sub array which is inversion-free.
# author  : Sahraoui Mohammed Taher Amine.
test = int(input())
while test:
    array = []
    inversion = True
    delete    = 0
    size  = int(input())
    array = input().split(" ")
    i = 0
    for element in array:
        array[i] = int(element)
        i = i + 1
    #search for inversions
    i = -1
    j = i + 1
    
    while (size > 1) and (inversion == True):
    #loop correctly
        i = i + 1
        j = j + 1
    #if the last array is inversion-free, get out from the loop + delete it
        if i == size - 1:
            print("delete: ", array[0:i+1])
            del array[:]
            delete = delete + 1
            inversion = False
            print("rest: ", array)
            continue
            
    #delete the array inversion-free statring from 0 to the point inversion occurs        
        if i < j and array[i] > array[j]:
            print("delete: ", array[0:i+1])
            del array[0:i+1]
            delete = delete + 1
            i = -1
            j = i + 1
            size = len(array)
            print("rest: ", array)
    
    #delete if it stays only 1 element    
    if size == 1:
        print("delete: ", array)
        del array[:]
        delete = delete + 1
        print("rest: ", array)

    print("number of inversion-free sub-arrays = ", delete)
    test = test - 1
        
        

   





