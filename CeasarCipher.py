import string

def cipher(s,k):
    
    # stores our final string
    output = []

    # get separate lists for upper and lower case
    alpha_upper = list(string.ascii_uppercase)
    alpha_lower = list(string.ascii_lowercase)
    
    alpha_len = len(alpha_upper)

    # remove any padding spaces in the string
    s = s.strip()

    for x in s:
        # If current char is an alphabet proceed with cipher
        # otherwise append the char to the output list
        if x.isalpha():
            # Upper case cipher
            if x.isupper():
                for i in range(alpha_len):
                    if x == alpha_upper[i]:
                        index = alpha_upper.index(x)
                        pos = (index + k) % (alpha_len)
                        output.append(alpha_upper[pos])
            # Lower case cipher
            else:
                for i in range(alpha_len):
                    if x == alpha_lower[i]:
                        index = alpha_lower.index(x)
                        pos = (index + k) % (alpha_len)
                        output.append(alpha_lower[pos])
        else:    
            output.append(x)
    
    result = ''.join(map(str,output))

    print(type(result))
    return result

s = "ab-middle-Oout-xyz" 
n = 2
print(cipher(s,n)) #cd-okffng-Qqwv-zab
