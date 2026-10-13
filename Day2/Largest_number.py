class Solution:
    def largest(self, arr):
        Largest= arr[0];
        for i in range(len(arr)):
            if arr[i]>=Largest:
                Largest= arr[i];
                
        return Largest
