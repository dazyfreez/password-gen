import string
import random
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
	length = int(input("Enter password length: "))
	random.shuffle(characters)
	password = []
	for i in range(length):
		password.append(random.choice(characters))
	random.shuffle(password)
	print("".join(password))
    password = "".join(password)
generate_random_password()
print("do you want to save your password? (y/n)")
if input() == "y":
    with open("password.txt", "w") as f:
        f.write("".join(password))
    print("password saved")