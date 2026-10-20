class Solution:
    def trimMean(self, arr):
        arr.sort()
        cut = len(arr) // 20
        total = 0
        for i in range(cut, len(arr) - cut):
            total += arr[i]
        return total / (len(arr) - 2 * cut)
        
