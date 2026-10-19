#Day 9

#Problem 1: Remove Duplicates from Sorted Array 

Remove duplicates in-place from a sorted array, return count of unique elements
Slow pointer marks where next unique element goes, fast pointer scans forward
When nums[fast] != nums[slow], move slow forward and copy the value
Return slow + 1 as the count
Time: O(n), Space: O(1)

#Problem 2: Move Zeroes 

Move all zeroes to the end, keep order of non-zero elements
Slow pointer marks where next non-zero should go, fast scans forward
When nums[fast] != 0, swap nums[slow] and nums[fast], move slow forward
Time: O(n), Space: O(1)

#Problem 3: Remove Element 

Remove all occurrences of a given value in-place, return count of remaining elements
Same pattern as Move Zeroes — skip val instead of 0
When nums[fast] != val, swap and move slow forward
Return slow as the count
Time: O(n), Space: O(1)
