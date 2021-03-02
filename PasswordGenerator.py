import random
passlength = int(input("enter the length of password : "))
randomvalue ="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&*"
password = "".join(random.sample(randomvalue,passlength))
print(password)
