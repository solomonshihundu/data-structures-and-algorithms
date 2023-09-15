#Binary Search Implementationx
#1 Pick the middle number in the list
#2 if it matches our number, return the number
#3 if its greater than our number, then number is to the right 
# of the list, if its less than our number, then number
# is to the left of the midpoint, search the appropriate side
# if not found return -1
def locate_card_binary(cards,query):

    # initialize the upper and lower bounderies
    lo, hi = 0, len(cards) - 1

    # loop through the cards making
    # sure we are within the bounderies
    while lo <= hi :
        midpoint = (lo + hi) // 2
        midcard = cards[midpoint]

        print("lo :", lo," hi :", hi," midpoint :", midpoint," midcard :",midcard)

        # middle card matches our search
        if midcard == query:
            return midpoint
        # explore the right side
        elif midcard > query:
            hi = midpoint-1
        # explore the left side
        elif midcard < query:
            lo = midpoint+1
            

    return -1

cards = [1,3,5,8,11,14,15,18,20,23,26,29,31]
pick = 11

result = locate_card_binary(cards,pick)
print(result,"\n")


