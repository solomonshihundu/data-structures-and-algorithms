# binary search method that takes
# upper and lower bounds of the data set
# and a condition method that determines 
# the direction of search
def binary_search(lo,hi,condition):
    while lo <= hi:
        mid = (lo+hi) // 2
        result = condition(mid)

        #print("lo :", lo," hi :", hi," midpoint :", mid," midcard :",cards[mid])

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

#Function encloser
def locate_cards_gen(cards,query):
    
    def condition(midpoint):
        if cards[midpoint] == query:
            if midpoint-1 >= 0 and cards[midpoint-1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[midpoint] < query:
            return 'right'
        else:
            return 'left'
    
    return binary_search(0,len(cards) - 1, condition)


# cards = [1,3,5,8,11,14,15,18,20,23,26,29,31]
# pick = 26

cards = [5]
pick = 5

result = locate_cards_gen(cards,pick)
print(result,"\n")
