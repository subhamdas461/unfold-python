import random
import string

def genPassword():
    total = string.ascii_letters + string.digits + string.punctuation

    length = 16

    password = "".join(random.sample(total, length))
    return password

pwd = genPassword()
print("Your password: "+ pwd)