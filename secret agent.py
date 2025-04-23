
code1 = input()
code2 = input()
code3 = input()
numA = int(input())
numB = int(input())


code1 = code1.lower()
code2 = code2.lower()
code3 = code3.lower()

if not (code1.isalpha() and code2.isalpha() and code3.isalpha()):
    print("Invalid codeword")
    exit()

if numA < 1 or numB < 1:
    print("Invalid numbers")
    exit()

combined = code1 + "-" + code2 + "-" + code3

secret_number = (numA * numB) + numA - numB

numA = numA + numB
numB = numA - numB
numA = numA - numB
swapped_A = numA
swapped_B = numB

avg_value = (swapped_A + swapped_B) / 2

message_length = len(combined)


no_hyphens = combined.replace("-", "")
is_palindrome = no_hyphens == no_hyphens[::-1]


print("Secret Code:", combined)
print("Secret Number:", secret_number)
print("Swapped Values: A=" + str(swapped_A) + ", B=" + str(swapped_B))
print("Average of Originals:", avg_value)
print("Combined Length:", message_length)
print("Palindrome:", is_palindrome)





