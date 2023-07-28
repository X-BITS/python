# version : python 3.9   
# desc    : find the maximum number n from nth combination of subnumbers of n taking k number of digits away.
# author  : Sahraoui Mohammed Taher Amine.

def treat(number):
    l = [n for n in number]
    total = 0
    for i in range(len(l)):
        l[i] = int(l[i])
        total += l[i]
    if total % 4 == 0:
        return True

test = int(input())      
while test:
    flag = False 
    a = int(input())
    while not flag:
        flag = treat(str(a))
        if flag:
            break;
        else:
            a = int(a) + 1
    print(a)         
    test = test - 1