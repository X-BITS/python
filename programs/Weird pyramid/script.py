# version : python 3.9   
# desc    : delete duplication from a given list
# author  : Sahraoui Mohammed Taher Amine.
number_blocks = int(input("input the number of blocks:"))
i = 1
h = 1
t = i
String = "[]"
print(String, "    =========> rank 1")
while i < number_blocks :
    if (i + (t + 1)) > number_blocks:
        break
    t += 1
    i += t
    String += "[]"
    h += 1
    print(String, "    =========> rank", h)
    

print("The height of the pyramid:", h)
