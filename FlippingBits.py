def flip_bits(num):
    
    # use string formatting to conver decimal to 32 bit binary string 
    result = ('{:032b}'.format(num))
    print(result)
    # stores the inverted binary result
    invers = ''

    # looping through the result of decimal to 32 bit binary conversion
    for i in result:
        # if we encounter a 0, append a 1 to our output variable
        if i == '0':
            invers += '1'
        # if we encounter a 1, append a 0 to our output varibale
        else:
            invers += '0'
    
    # convert the inverted binary string to decimal
    print(int(invers,2))

num = 4
flip_bits(4)