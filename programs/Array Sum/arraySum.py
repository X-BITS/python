# Taking data dynamicaly in one single string separated by white spaces
n = int(input())
numbers_string = input().split(" ")
numbers       = []

for number_str in numbers_string:
    numbers.append(int(number_str))

Sum = 0
for i in range(0,len(numbers)):
    Sum += numbers[i]
print(Sum)

# Taking data dynamically one by one.
# Dynamic input of data, then calculation of the sum
#array = []
#n = int(input())
#Sum = 0
#for i in range(0,n):
    #number = int(input())
    #array.append(number)
    #Sum += array[i]
#print(Sum)