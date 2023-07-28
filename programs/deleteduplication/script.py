# version : python 3.9   
# desc    : delete duplication from a given list
# author  : Sahraoui Mohammed Taher Amine.
#--------------------------------------------
# removing dup from a list by creating a set up on that list so dup will be deleted automatically

# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# my_list = list({item for item in my_list})
# print("The list with unique elements only:")
# print(my_list)

#--------------------------------------------

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print(my_list)
n = len(my_list)
i = 0
while i < n:
    j = i + 1 
    while j < n:
        if my_list[i] == my_list[j]:
            del my_list[j]
            n = n - 1
            i = 0
        j = j + 1
    i = i + 1
print("The list with unique elements only:")
print(my_list)

