import random
number = random.randint(1, 10)
guss = int(input("Guss a number between 1 and 10: "))
while guss != number:
    if guss < number:
        print("Too low!")
    else:
        print("Too high!")
    guss = int(input("Guss again: "))
print ("Congratulations! You guessed the number.")