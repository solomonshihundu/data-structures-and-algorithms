class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def direction(self,nums,target,midpoint):
            if target == nums[midpoint]:
                return 'found'
            elif target > nums[midpoint]:
                return 'right'
            else:
                return 'left'
            
            
        def perform_search(self):

            lo = 0
            hi = len(nums)-1

            while lo <= hi:
                midpoint = len(lo + hi) // 2
                self.midpoint = midpoint

                result = direction(self,self.nums,self.target,self.midpoint)

                if result == 'found':
                    return self.midpoint
                elif result == 'left':
                    hi = midpoint-1
                else:
                    lo = midpoint+1
            return -1
        
    self.perform_search()
    

if __name__ == '__main__':
    arr = [-1,0,3,5,9,12]
    x = 9
    result = Solution.search()
    print(result)