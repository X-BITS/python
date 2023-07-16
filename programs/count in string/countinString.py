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