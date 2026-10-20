class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        sum=0
        for i in range(k):
            sum+=arr[i]
        best_sum=sum
        for i in range(k,len(arr)):
            sum+=arr[i]
            sum-=arr[i-k]
            if sum>best_sum:
                best_sum=sum
        return best_sum
