# # True Lova Calculator
# print("Welcome to True Love Calculator")
# name1 = input("Enter Your Name: ").lower()
# name2 = input("Enter Your Crush Name: ").lower()

# combined_names = name1 + name2

# t = combined_names.count("t")
# r = combined_names.count("r")
# u = combined_names.count("u")
# e = combined_names.count("e")
# l = combined_names.count("l")
# o = combined_names.count("o")
# v = combined_names.count("v")
# e = combined_names.count("e")

# true = t + r + u + e 
# love =  l + o + v + e

# stringify = str(true) + str(love)
# score = int(stringify)

# if score < 30:
#     print(f"Your score is {score}%, You are not a good match")
# elif score < 65:
#     print(f"Your score is {score}%, You are Very Good Match")
# else:
#     print(f"Your score is {score}%, Amazing Wow!")



# print("Welcome To Pizza Hut!")
# size = input("Pizza Size? S, M, L").upper()
# add_pepperoni = input("Do You want to add pepperoni? Y or N.").upper()
# extra_cheese = input("Do you want extra cheese? Y or N.").upper()
# bill = 0

# if size == "S":
#     bill = 15
# elif size == "M":
#     bill = 20
# else:
#     bill = 25
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 5
# else:
#     bill

# if extra_cheese == "Y":
#         bill +=1

#         print(f"Your bill is {bill}")

# prices = {"S" : 15, "M" : 20, "L" : 25}
# bill = prices[size]

# if extra_cheese == "Y":
#     bill += 3 if size == "S" else 5

# if add_pepperoni == "Y":
#     bill += 6 if size == "S" else  10

# print(f"Your bill is {bill}")        

# print("Welcome to the Roller Coaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
# if height >=120:
#     print("You can ride the roller coaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Your Ticket is 5$")
#     elif age < 18:
#         bill = 7
#         print("Your ticket is 7")
#     elif age >= 40 and age <= 45:
#         bill = 0
#         print("Your ticket is free")
#     else:
#         bill += 18
#         print("Your ticket is $18")
#     want_photo = input("Do  you want photo taken? Y or N.").upper()

#     if want_photo == "Y":
#         bill += 3
#         print(f"Your Bill is ${bill}")
#     else:
#         print(f"Your bill is: ${bill}")
# else:
#     print("Sorry, you have to grow taller before you can ride.")
    


# # Even And Odd
# print("Check If number is even or odd!")
# number = int(input("Enter a Number "))

# check = number % 2

# if check == 0:
#     print(f"The Number {number} is Even")
# else:
#     print(f"The Number {number} is odd")

#     # or 

#     if number % 2 == 0:
#         print("This number is Even")
#     else:
#         print("This number is odd")

# # Advance BMI Calculator

# height = float(input("Wha is your height in m? "))
# weight = int(input("What is your weight in kg? "))

# bmi = round(weight / height ** 2)


# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, Under Wight")
# elif bmi < 25:
#     print(f"Your BMi is {bmi}, Normal Weight")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, Over Weight")
# elif bmi < 35:
#     print(f"Your BMI is {bmi}, Obese")
# else:
#     print(f"Your BMi is {bmi}, Clinically Obese")

# # Leap Year Checker

# year = int(input("Enter Year: "))

# if year % 4 == 0:
#     print("Proceeding to next step")
#     if year % 100 != 0:
#         print("Leap Year")
#     elif year % 400 == 0:
#         print("Leap Year")
#     else:
#         print("Not a Leap Year")
# else:
#     print("Not a Leap Year")

#     # or 

#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 print("Leap Year")
#             else:
#                 print("Not a Leap Yer!")
#         else:
#             print("Leap Year")
#     else:  
#         print("Not a leap year.")