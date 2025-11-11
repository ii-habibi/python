# import random

# # user_input = input("Choose your hand. Rock R, Paper P, Scissors S ").upper()

# # com_input = ""
# # random_number = random.randint(1, 3)

# # hands = {"R": "Rock", "P": "Paper", "S": "Scissors" }

# # if random_number == 1:
# #     com_input = "R"
# # elif random_number == 2:
# #     com_input = "P"
# # else:
# #     com_input = "S"

# # print(f"You chose: {hands.get(user_input, 'Invalid')}")
# # print(f"Computer chose: {hands[com_input]}")

# # if user_input == com_input:
# #     print("It's a tie!")
# # elif (user_input == "R" and com_input == "S") or \
# #         (user_input == "P" and com_input == "R") or \
# #         (user_input == "S" and com_input == "P"):
# #     print("You Win!")
# # elif user_input in hands:
# #     print("Computer Wins!")
# # else:
# #     print("Invalid Input. Please Choose R, P, S.")

# # Banker rouellete
# name_String = input("Give me name of each person seprated by comma ( , )")

# split_names = name_String.split(",")

# print(f"This is random: {random.randint(0, len(split_names)-1)}")

# # result = split_names[random.randint(0, len(split_names)-1)]
# result =  random.choice(split_names)

# print(result)


# row1 = ["📋", "📋", "📋"]
# row2 = ["📋", "📋", "📋"]
# row3 = ["📋", "📋", "📋"]


# position = list(input("Where do you want place it? "))

# col = position[0]
# row = position[1]

# map = [row1, row2, row3]
# map[int(row)-1][int(col)-1] = "X"
# print(f"{row1}\n{row2}\n{row3}")