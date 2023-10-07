import string

def pangrams(str):
    
    # store all the alphabets in list
    alpha = list(string.ascii_lowercase)

    # vars to check for presence of alpha
    is_pan = True

    # remove spaces in the sring
    str = str.replace(" ","").lower()
    
    # create list of all the characters present in the input string
    letters = [x for x in str]

    # going through the list of all aphabets, 
    # check if our list has all of them
    for i in range(len(alpha)):
        if alpha[i] not in letters:
            is_pan = False
    
    if is_pan:
        print("Pangram")
    else:
        print("Not Pangram")

    
str = 'Hello World'
str1 = 'The quick brown fox jumps over the lazy dog'

pangrams(str)