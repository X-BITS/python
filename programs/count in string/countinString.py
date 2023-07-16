# title: count in string
# desc: counting the total number of character k occurs in string S
# author: Sahraoui mohammed taher amine.
# S= String, k = specific character, T = number of test  of the function solve.  
def solve (S, k):
    n = 0
    for c in S:
        if c == k:
            n += 1            
    return n

T = int(input())
for _ in range(T):
    S = input()
    k = input()

    out_ = solve(S, k)
    print (out_)
