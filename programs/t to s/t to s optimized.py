def solve():
    n = int(input())
    s = input().strip()
    t = input().strip()
    freq = [0] * 26
    for i in range(n):
        freq[ord(t[i]) - ord('a')] += 1
    ct = 0
    for i in range(n):
        if s[i] != '?':
            freq[ord(s[i]) - ord('a')] -= 1
        else:
            ct += 1
    for i in range(26):
        if freq[i] < 0:
            print("No")
            return
    print(freq)
    print("Yes")

def main():
    t = int(input())
    for _ in range(t):
        solve()
        print()

if __name__ == "__main__":
    main()
   
