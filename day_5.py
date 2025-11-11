import random
# student_height = input( "Enter Heights of the student: ").split()

# for n in range(0, len(student_height)):
#     student_height[n] = int(student_height[n])

# h = 0
# l = 0

# for n in  student_height:
#     h = h + n
#     l = l+1

# marks = input("Enter Marks of the student: ").split()

# for n in range(0, len(marks)):
#     marks[n] = int(marks[n])

# heighest = 0

# for score in marks:
#     if score > heighest:
#         heighest = score

# print(heighest)


# for n in range(1, 101):
#     print("Fizz"*(n%3==0) + "Buzz"*(n%5==0) or n)


# [print("Fizz"*(n%3==0) + "Buzz"*(n%5==0) or n) for n in range(1, 101)]

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
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+"]
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))
for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")
