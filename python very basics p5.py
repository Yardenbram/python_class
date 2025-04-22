print("let's check it the experiment is safe or not")
temperature = float(input("Enter the temperature in celcluse: "))
pressure = float(input("Enter the pressure in Atm: "))
voltage = float(input("Enter the voltage in volts: "))
if temperature >= 20 and temperature <= 80 and pressure < 50 and voltage >=200 and voltage <= 250:
    print("The experiment is safe")
else:
    print("The experiment is not safe")