print("you are under evaluation")
Wizard = input("enter your name: ")
print("Welcome", Wizard)
spell_power = int(input("enter your spell power between 0 to 100: "))
accuracy = int(input("enter your accuracy between 0 to 100: "))
control = int(input("enter your control between 0 to 100: "))
average = (spell_power + accuracy + control) / 3
if average >= 90:
    print(Wizard, "You are an Archmage")
elif average >= 75 and average < 90:
    print(Wizard, "You are a Mage")
elif average >= 60 and average < 75:
    print(Wizard, "You are an apprentice")
elif average < 60:
    print(Wizard, "You are a failure")