import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
print(" Welcome to PyPassword Generator! ")
ps_letters = int(input(" How many letters would you like to have in your password? \n"))
ps_symbols = int(input(" How many symbols would you like to have in your password? \n"))
ps_numbers = int(input(" How many numbers would you like to have in your password? \n"))
password_list = []
last_used_password = []

for char in range(1, ps_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, ps_symbols + 1):
    password_list += random.choice(symbols)
for char in range(1, ps_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)
password = "".join(password_list)
print(f"Your Password is: {password}")
last_used_password.append(password)
print(last_used_password)
