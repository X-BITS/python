from pwn import *
import sys


if len(sys.argv) != 2:
    print("invalid command")
    print(f"> {sys.argv[0]} <sha256checksum>")
    sys.exit(1) #error 1 indicate invalid execution because of missing arguments
target = sys.argv[1]
passwordfile = "/usr/share/wordlists/rockyou.txt"
attempts = 0

with log.progress(f"Attempting crack {target}!\n\n") as ps:
    with open(passwordfile, "r", encoding="latin-1") as passwordlist:
        for password in passwordlist:
            password      = password.strip("\n").encode('latin-1')
            password_hash = sha256sumhex(password)
            ps.status("[{}] {} == {}".format(attempts, password.decode("latin-1"), password_hash))
            if password_hash == target:
                ps.success(f"Password found! : hash{target}: password: {password.decode('latin-1')}")
                sys.exit(0) #succefully exiting the script
            attempts += 1
        else:
            ps.failure(f"No valid password found! for hash: {target}")




