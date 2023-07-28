# version : python 3.9   
# desc    : find the special number n . A number n is said to be special if the sum of its digits is divisible by 4. 
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
