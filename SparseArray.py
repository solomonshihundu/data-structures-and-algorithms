from collections import Counter
# Methods that returns the number of times the
# query strings appear in the input (strings) 
# array 
def matchingString(strings,query):
    string_counter = Counter(strings)
    print([string_counter[q] for q in query])
    

input_string = ['ab','ab','abc']
queries = ['ab','abc','bc']

matchingString(input_string,queries)

# def match_string(strings,query):
#     count = {}
#     for i in strings:
#         for j in query:
#             if j == i:
#                 count[j] = 1

#             if j not in count:
#                 count[j] = 1
#             else:
#                 count[j] += 1

