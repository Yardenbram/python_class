age = int(input("Enter your age: "))
day = str(input("Enter weekday or weekend: ")).lower()
loylty_member = str(input("Are you a loyalty member? (yes/no): ")).lower()
if age < 0:
    print("Invalid age")
    exit()
if day != "weekday" and day != "weekend":
    print("Invalid day")
    exit()
ticket_price = 20
if age < 13:
    ticket_price = ticket_price * 0.5
elif age >= 60:
    ticket_price = ticket_price * 0.7
if day == "weekend":
    ticket_price = ticket_price + 5
else:
    ticket_price = ticket_price
if loylty_member == "yes":
    ticket_price = ticket_price -2
else:
        ticket_price = ticket_price
print("The ticket price is: ", ticket_price)