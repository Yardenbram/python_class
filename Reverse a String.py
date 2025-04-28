def reverse_string(s):

    return s[::-1]

string = str(input("Enter a string to reverse: "))
reversed_string = reverse_string(string)
print(f"The reversed string is: {reversed_string}")