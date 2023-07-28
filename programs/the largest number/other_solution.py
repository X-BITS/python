# version : python 3.9   
# desc    : find the maximum number n from nth combination of subnumbers of n taking k number of digits away.
# author  : Sahraoui Mohammed Taher Amine.

def solve(n, k):
    for j in range(k):
        ans = 0
        i = 1
        while n // i > 0:
            temp = (n // (i * 10)) * i + (n % i)
            i *= 10
            ans = max(ans, temp)
        n = ans
    return n

if __name__ == "__main__":
    n, k = map(int, input().split())
    assert 1 <= n <= 1000000000000000000
    assert 1 <= k <= 3

    d = len(str(n))
    assert d >= k

    print(solve(n, k))
