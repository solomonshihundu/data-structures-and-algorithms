########################################################################################################
# Given only the number of pages
########################################################################################################

# Implementation of Binary Search
def page_count(arr,n,p,direction):
    # Get the middle page, it will help in determining
    # weather to start from the front or back of the book
    mid_point = n // 2
    result = direction(mid_point)

    # stores the number of times we have
    # flipped a page
    count = 1


    if result == "front":
        # First page of the book is empty thus
        # we start pos, at page obe
        pos = 2
        if p - 1 <= 0:
            count = 0
            return count
        else:
            while pos <= mid_point:
                if arr[pos] == p:
                    return count
                else:
                    pos += 2
                    count += 1
    else:
        # The last page of the book is also not numbered
        pos = n - 2
        if p + 1 >= n:
            count = 0
            return count
        else:
            while pos >= mid_point:
                if arr[pos] == p:
                    return count
                else:
                    pos -= 2
                    count += 1

        

def locate_page(n,p):

    # create a list equal to number of pages
    arr = list(range(1,n))

    print(arr)

    #Sort array in ASC order
    arr.sort()

    # method assists in establishing which direction 
    # to start with, if the page number is greater than
    # the mid point start from behind, else the page number
    # is less than the midpoint, start from the front
    def direction(mid_point):
    
        if mid_point-1 >= 0:
            if p <= arr[mid_point]:
                return("front")
            
            elif p >= arr[mid_point]:
                return("back")
            
    return page_count(arr,n,p,direction)


# arr = [1,3,2,5,4]
# arr = [1,3,8,2,5,7,6,4]
# 5 4 0
# 6 2 1
# 7 3 1
n = 6
page = 4
r = locate_page(n,page)
print(r)


# # Implementation of Binary Search
# def page_count(arr,n,p,direction):
#     # Get the middle page, it will help in determining
#     # weather to start from the front or back of the book
#     mid_point = n // 2
#     result = direction(mid_point)

#     # stores the number of times we have
#     # flipped a page
#     count = 1


#     if result == "front":
#         # First page of the book is empty thus
#         # we start pos, at page obe
#         pos = 1
#         while pos <= mid_point:
#             if arr[pos] == p:
#                 return count
#             else:
#                 pos += 1
#                 count += 1
#     else:
#         # The last page of the book is also not numbered
#         pos = n - 1
#         while pos >= mid_point:
#             if arr[pos] == p:
#                 return count
#             else:
#                 pos -= 1
#                 count += 1

        

# def locate_page(arr,n,p):

#     #Sort array in ASC order
#     arr.sort()

#     # method assists in establishing which direction 
#     # to start with, if the page number is greater than
#     # the mid point start from behind, else the page number
#     # is less than the midpoint, start from the front
#     def direction(mid_point):
    
#         if mid_point-1 >= 0:
#             if p <= arr[mid_point]:
#                 return("front")
            
#             elif p >= arr[mid_point]:
#                 return("back")
            
#     return page_count(arr,n,p,direction)


# arr = [1,3,2,5,4]
# # arr = [1,3,8,2,5,7,6,4]
# n = len(arr)
# page = 5
# r = locate_page(arr,n,page)
# print(r)


