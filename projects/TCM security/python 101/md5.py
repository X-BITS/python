import hashlib
import sys

def check_password(md5_hash, password_file):
    try:
        with open(password_file, 'r') as file:
            for line in file:
                password = line.strip()
                hashed_password = hashlib.md5(password.encode()).hexdigest()
                if hashed_password == md5_hash:
                    print(f"Match found: {password}")
                    return
        print("No match found.")
    except FileNotFoundError:
        print(f"File not found: {password_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <md5_hash> <password_file>")
    else:
        md5_hash = sys.argv[1]
        password_file = sys.argv[2]
        check_password(md5_hash, password_file)
