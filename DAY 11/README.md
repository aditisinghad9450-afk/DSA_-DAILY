#Day 11 

#Problem 1: Maximum Average Subarray I (LC 643)

Calculate sum of first k elements in one loop
Second loop slides the window: sum += nums[j], sum -= nums[j-k]
Track best_sum and compare at each step
Return best_sum / k
Time: O(n) | Space: O(1)

Problem 2: Max Sum Subarray of Size K

Identical sliding window pattern
Same as Problem 1 but return best_sum instead of dividing by k
Time: O(n) | Space: O(1)

Problem 3: Mean of Array After Removing Some Elements (LC 1619)

Sort the array first
Calculate cut = len(arr) // 20 (5% of elements)
Sum elements from index cut to len(arr) - cut
Divide by the number of elements summed: len(arr) - 2 * cut
Time: O(n log n) for sort | Space: O(1)

            
