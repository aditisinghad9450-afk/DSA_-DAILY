class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n= len(nums)
        sum=0
        diff=0
        for i in range(len(nums)):
            exp_sum =n*(n+1)//2
            sum+=nums[i]
            diff= exp_sum-sum

        return diff





        
