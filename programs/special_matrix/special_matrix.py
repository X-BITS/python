def f():
    n, m = map(int, input().split())
    assert 1 <= n <= 1000000
    assert 1 <= m <= 1000000

    if n < m:
        n, m = m, n

    ans = 0
    for i in range(1, n + 1):
        tot = min(i, m)
        ans += v[i + 1] * tot

    tot = m - 1
    for i in range(2, m + 1):
        ans += v[n + i] * tot
        tot -= 1

    print(ans)


test_case = 1

Mx = 2 * 10**6 + 5
p = [1] * (Mx + 5)
v = [0] * (Mx + 5)
p[0] = p[1] = 0

for i in range(2, Mx):
    if p[i]:
        for j in range(i, Mx, i):
            v[j] += 1
            p[j] = 0

t = 1
if test_case:
    t = int(input())
assert 1 <= t <= 10

for _ in range(t):
    f()
