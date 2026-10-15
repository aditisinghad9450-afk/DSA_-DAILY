class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        current=0
        best=0
        for i in range(len(nums)):
            if nums[i]==1:
                current+=1
            else:
                if current>best:
                    best=current
                current=0
        if current>best:
            best=current
        return best
