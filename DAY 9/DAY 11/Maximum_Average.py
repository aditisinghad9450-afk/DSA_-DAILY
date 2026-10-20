class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        sum=0
        for i in range(k):
            sum+=nums[i]
        best_sum=sum
        for j in range(k,len(nums)):
            sum+=nums[j]
            sum-=nums[j-k]
            
            if sum>best_sum:
                best_sum=sum

        return best_sum/k




        




        

        
