import string, random

lowers = list(string.ascii_lowercase)
uppers = list(string.ascii_uppercase)
symbols = list(string.punctuation)
numbers = [str(item) for item in range(0,10)]

all_list = lowers+uppers+symbols+numbers
ranges = len(all_list)

while True:
    pass_lenght = input("Enter password lenght: ")
    if int(pass_lenght) < 3:
        print("Password must be at least 3 char")
    else:
        break
def generate(lenght):
    for _ in range(4):
        random.shuffle(all_list)

    password = ''
    for i in range(int(lenght)):
        new = random.randint(0,int(lenght))
        password += all_list[new]
    return password

while True:
    password = generate(pass_lenght)
    if ((any(char.isdigit() for char in password)) and (any(char.isalpha() for char in password)) and (any(not c.isalnum() for c in password))):
        print(password)
        break
    else:
        continue

