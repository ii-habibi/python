# two_digit_number = input("Type a two digit number: ")

# first_digit = two_digit_number[0]
# second_digit = two_digit_number[1]

# print(int(first_digit) + int(second_digit))

# # now mathimatical operators
# 3 + 5
# 7 - 4
# 3 * 2
# 6 / 3
# 2 ** 3  # 2 to the power of 3 = 2 * 2 * 2
# print(3 * (3 + 3) / 3 - 3)
# # PEMDAS - Parentheses, Exponents, Multiplication, Division, Addition, Subtraction
# # Left to right for same precedence

# print(3 * 3 + 3 / 3 - 3)  # 9 + 1 - 3 = 7.0
# print(3 * (3 + 3) / 3 - 3)  # 3 * 6 / 3 - 3 = 6.0

# # BMI Calculator
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")

# bmi = int(weight) / float(height) ** 2
# print(int(bmi))

# # Rounding Numbers
# print(round(8 /3 , 2))

# # this is the floor division without using int converstion 

# print(8 // 3) # result is 2

# # f-String 
# score = 0
# height = 1.8

# print(f"your score is {score}, your height is {height}, your BMI is {bmi}")

# # week and days left exercise

# age = input("What is your current age? ")
# age_as_int = int(age)
# years_remaining = 90 - age_as_int
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52

# print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {years_remaining} years left.")

# Bill Tip Calculator 

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")
