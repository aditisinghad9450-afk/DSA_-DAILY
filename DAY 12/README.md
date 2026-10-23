#Day 12

#Problem 1: Minimum Size Subarray Sum

Expand right, add nums[right] to total
While total >= target: record window length, subtract nums[left], shrink left
Track best = min(best, right - left + 1)
Start best = float('inf') since looking for minimum
Time: O(n) 
Space: O(1)

#Problem 2: Longest Subarray with Sum K 

Same expand/shrink pattern
While total > k: shrink from left
If total == k: update best = max(best, right - left + 1)
Start best = 0 since looking for maximum
Note: sliding window only works with positive numbers. Negatives need prefix sum + hashmap
Time: O(n)
Space: O(1)

#Problem 3: Fruit Into Baskets

Sliding window + hashmap
Dict tracks count of each fruit type in window
Expand right: add fruits[right] to dict using .get()
While len(basket) > 2: decrease count of fruits[left], delete key if count is 0, move left
Track best = max(best, right - left + 1)
Time: O(n) 
Space: O(1)
