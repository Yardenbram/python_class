driver_age = int(input("Enter driver age: "))
number_of_accidents = int(input("Enter number of accidents: "))
if driver_age < 25:
    primum = 3000
else:
    primum = 2000
if number_of_accidents == 0:
    primum = primum + 0
else:
    primum = primum + 500 * number_of_accidents
if primum > 5000:
        print("your primum is ", primum)
        print("you are a high risk driver")
else:
        print("your primum is ", primum)
        print("you are a stardart driver")