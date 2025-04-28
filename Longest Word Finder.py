
def longest_word(list_of_strings :list) -> tuple : 
    if not isinstance(list_of_strings,list) or list_of_strings is None:
        print("ililagel argument")
        return 
    max_length = 0
    word =  None  
    for string in list_of_strings: 
        if string is not None and len(string) > max_length:
            max_length = len(string)
            word = string
    if word is None:
        print("list is empty")
        return
    return max_length , word


print(longest_word(["a",None,"ABC"]))