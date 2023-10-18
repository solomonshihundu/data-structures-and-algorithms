import string

def cipher(s,n):
    
    output = []

    alpha_upper = list(string.ascii_uppercase)

    alpha_lower = list(string.ascii_lowercase)

    s = s.strip()

    for x in s:
        if x.isalpha():
            if x.isupper():
                for i in range(len(alpha_upper)):
                    if x == alpha_upper[i]:
                        if i+n > len(alpha_upper):
                            i = n - i
                            output.append(alpha_upper[i+n])
                        else:
                            output.append(alpha_upper[i+n])
            else:
                for j in range(len(alpha_lower)):
                    if x == alpha_lower[j]:
                        if j + n > len(alpha_lower):
                            j = n - j
                            output.append(alpha_lower[j+n])
                        else:
                            output.append(alpha_lower[j+n])
        else:
            output.append(x)
    
    result = ' '.join(map(str,output))
    return result

s = "middle-Outxyz" 
n = 2
print(cipher(s,n)) #okffng-Qwvb