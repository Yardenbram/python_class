age = int(input("enter your age"))
black_list = input("black list yes/no").lower() == "yes"
royal_family = input ("royal family yes/no").lower() == "yes"
gold_pass = input("gold pass yes/no").lower() == "yes"
if age >= 18 and not black_list and (royal_family or gold_pass):
    print ("come in")
else:
     print ("go away")



