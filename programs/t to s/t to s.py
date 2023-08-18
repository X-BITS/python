def check_chars(s, t):
    s = s.lower()
    t = t.lower()
    for char in s:
        if char not in t and char != '?':
            return False
        
    if fast_eliminate(s, t):
        return False
    
    return True

def fast_eliminate(a, b):
    def count_characters(s):
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        return char_count

    a_counts = count_characters(a)
    b_counts = count_characters(b)
    
    for char in a:
        if char in b and char != '?':
            if a_counts[char] > b_counts[char]:
                return True
    return False

def is_clear(s):
    for char in s:
        if char == '?':
            return False
    return True

def is_t_in_s(s, t):
    for char in t:
        if char not in s:
            return False
    return True

def character_occurrence(a, b):
    def count_characters(s):
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        return char_count

    a_counts = count_characters(a)
    b_counts = count_characters(b)
    return a_counts == b_counts

def check_combs(a, b):
    def count_characters(s):
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        return char_count

    a_counts = count_characters(a)
    b_counts = count_characters(b)
    #print(a_counts, b_counts)
    for key in a_counts.keys():
        if key in b_counts and key != '?':
            b_counts[key] = b_counts[key] - a_counts[key]
    
    for key in b_counts.keys():
        if b_counts[key] < 0:
            a_counts['?'] = a_counts['?'] + b_counts[key]
    #print(a_counts, b_counts)
    total = 0
    for key in b_counts.keys():
        total += b_counts[key]

    if total == a_counts['?']:
        return True
    else:
        return False

test   = int(input())
while test > 0:
    lenght = int(input())
    s      = input()
    t      = input()
    while len(s) > lenght or len(t) > lenght:
        s      = input()
        t      = input()
    if check_chars(s, t):
        if is_clear(s):
            if is_t_in_s(s, t):
                if character_occurrence(s, t):
                    print('Yes')
                else:
                    print('No')
            else:   
                print('No')
        else:
           if check_combs(s, t):
                print('Yes')
           else:
                print('No')
    else:
        print('No')
    test -= 1
