# Considering that flipping a page will cover
# two numbers, then the modulus of the page number
# will give the number of flips , required to reach that
# page
def page_count(n, p):
    result = min(p // 2, (n // 2 - p // 2))
    print(result)

n = 5
p = 4

page_count(n,p)