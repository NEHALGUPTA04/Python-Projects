import random
min_val = 1
max_val = 6
roll = input("Rolling the dice ???(yes or no) : ")
while True:
    if roll== "yes":
        print("Rolling The Dices...")
        print("The Values are: ")

        print(random.randint(min_val, max_val))
        print(random.randint(min_val, max_val))

    roll_again = input("Roll again ??(yes/no): ")
    if roll_again != "yes":
        print("Thanks!!")
        break

