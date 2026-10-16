class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        s= set()
        n= len(nums)
        diff= set()
        for i in range(len(nums)):
            s.add(nums[i])
        for i in range(1,n+1):
            if i not in s:
                diff.add(i)
        return list(diff)



            
