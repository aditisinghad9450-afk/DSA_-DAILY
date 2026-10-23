class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left=0
        total=0
        best=float('inf')

        for right in range(len(nums)):
            total+=nums[right]


            while total>=target:
                best=min(best, right-left+1)
                total-=nums[left]
                left+=1

        if best==float('inf'):
            return 0

        return best

                


        
