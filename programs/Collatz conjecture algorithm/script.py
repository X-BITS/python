# version : python 3.9   
# desc    : calculating the number of steps for n going from it's starting value to 1. Collatz conjecture algorithm.
# author  : Sahraoui Mohammed Taher Amine.

n = int(input())
steps = 1
while n > 0:
    print(n)
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    if n == 1:
        break;
    steps += 1
print("steps = ", steps)