from collections import Counter

def match_pairs(arr):
    # list to hold all available pairs from arr
    pairs = []

    # Counter method returns a dictionary,
    # with the key being the unique elements in arr
    # and value being the frequency of occurance
    arr_dict = Counter(arr)

    # looping through the occurance of individual
    # values, get the non-remainder division of the
    # the occurance, hence the number of pairs, add the
    # results to a list and sum the list.
    for i in arr_dict.values():
        pairs.append(i // 2)
    print(sum(pairs))
    

#arr = [10,20,20,10,10,30,50,10,20]
arr = [4, 5 ,5, 5 ,6, 6 ,4 ,1 ,4 ,4 ,3 ,6 ,6 ,3 ,6 ,1 ,4 ,5 ,5 ,5]
match_pairs(arr)