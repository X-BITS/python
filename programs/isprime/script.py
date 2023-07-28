# version : python 3.9   
# desc    : check whether a given number is a prime number or not.
# author  : Sahraoui Mohammed Taher Amine.
def is_prime(num):
    for i in range(2, num):
        if num % i  == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
