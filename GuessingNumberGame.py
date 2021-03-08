import random as rd
number = rd.randint(1,100)
user_guess = int(input("Enter the number between 1 and 100 : "))
print("number generated: ")
print(number)                                                       #print("Random number :" + str(number))
while user_guess != True:
    if number != user_guess:
        print("Your guess is wrong, number does not match with your guess!!!!")
        if number > user_guess:
            print("Oww,Your guess is lower than number")
        elif number < user_guess:
            print("Oww,Your guess is greater than number")

    else:
        print("Wow, Your guess matched with the number.....Congratulations!!!!")
    break;