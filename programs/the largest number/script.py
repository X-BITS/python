# version : python 3.9   
# desc    : find the maximum number n from nth combination of subnumbers of n taking k number of digits away.
# author  : Sahraoui Mohammed Taher Amine.

nk = input().split(" ")

# k is the number of digits we must take each time                  
k = int(nk[1])
digits = []

# testing for right k
while k <= 0 or k > 3:
    nk = input().split(" ")
    k = int(nk[1])

# the creation of single digit list
for d in nk[0]:
    digits.append(d)

# Convert the digits to integers
digits = [int(d) for d in digits]

# The idea is to remove digits one by one from the original number
# to form the maximum number
stack = []
remaining_digits = len(digits) - k
for d in digits:
    while k > 0 and stack and stack[-1] < d:
        stack.pop()
        k -= 1
    stack.append(d)

# If 'k' is still greater than 0, we need to remove some digits from the end
result = stack[:remaining_digits]

# Convert the result back to a single integer
max_number = int("".join(map(str, result)))

print(max_number)

