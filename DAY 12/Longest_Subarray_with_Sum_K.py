class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        left=0
        total=0
        best=0
        for right in range(len(arr)):
            total+=arr[right]
            
            while total>k:
                total-=arr[left]
                left+=1
            if total==k:
                best=max(best,right-left+1)
    
                
        if best==0:
            return 0
        return best
    
