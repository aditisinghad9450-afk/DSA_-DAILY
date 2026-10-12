class Solution:
    def singleNumber(self, nums: list[int]) -> int:
       for i in range(len(nums)):
        unique=True
        for j in range(len(nums)):
            if i!=j and nums[i]==nums[j]:
                unique = False
                break
                 # Check if the same element appears elsewhere

        if unique:
            return nums[i]
