class Solution:
    def getSecondLargest(self, arr):
        # code here
        largest= arr[0]
        secondLargest=-1
        for i in range(1,len(arr)):
        
            if arr[i]> largest:
                secondLargest= largest
                largest=arr[i]
                
            elif arr[i]<largest:
                if secondLargest==-1 or arr[i]>secondLargest:
                    secondLargest=arr[i]
            
        return secondLargest
