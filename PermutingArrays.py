# n is the size of arrays
# k is the relational variable
# A,B arrays to permute
def permute_two_arrays(n,k,A,B):
    # logic for a successful permute
    # to occur, then the largest value in A
    # plus the smallest value in B should
    # yeild a value greater than or equal
    # to K. 

    # sort the arrays A in ASC, B in DESC order
    A.sort()
    B.sort(reverse= True)

    print(A)
    print(B)

    # use the zip function to create an iteratior of tuples 
    # from A and B i.e ((A[0],B[0]) .... (A[n],B[n])
    for a,b in zip(A,B):
        # get the sum of the values in the
        # tuples above, if the sum is less than 
        # relational var, hence not permutable 
        # return NO, else return YES
        if a + b < k:
            return "NO"
    return "YES"


A = [2,1,3]
B = [7,8,9]

# A = [1, 2, 2, 1]
# B = [3, 3, 3, 4]

n = len(A) # Arrays Size
k = 10 # Relational variable

result = permute_two_arrays(n,k,A,B)
print(result)