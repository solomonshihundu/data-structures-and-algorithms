class Solution:
    
    def __init__(self,nums,target):
        self.nums = nums
        self.target = target

    def search(self):

        nums = self.nums
        target = self.target

        def direction(nums,target,midpoint):
            if nums[midpoint] == target and midpoint-1 >= 0:
                if nums[midpoint-1] == target:
                    return 'left'
                else:
                    return 'found'
            elif target > nums[midpoint]:
                return 'right'
            else:
                return 'left'
            
        lo = 0
        hi = len(nums)-1

        while lo <= hi:
            
            midpoint = (lo + hi) // 2
            result = direction(nums,target,midpoint)

            if result == 'found':
                return midpoint
            elif result == 'left':
                hi = midpoint-1
            else:
                lo = midpoint+1
        return -1

def test_search():
    arr = [-1,0,3,5,9,12]
    x = 9
    result = Solution(arr,x)
    return result

    

if __name__ == '__main__':
    soln = test_search().search()
    print(soln)