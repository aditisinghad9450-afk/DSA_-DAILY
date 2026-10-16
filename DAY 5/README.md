#Intersection of Two Arrays 

Approach: Put all elements of nums1 into a set. 
Walk nums2, check each element against the set. 
If found, add to a result set. Return as list.
Time: O(n + m) — one pass per array
Space: O(n) — set for nums1 + result set

#Missing Number

Approach: Calculate expected sum of 0 to n using formula n*(n+1)//2. 
Subtract actual sum of array. 
The difference is the missing number.
Time: O(n) — single pass to sum
Space: O(1) — just variables

#Find All Numbers Disappeared in an Array 

Approach: Add all array elements to a set.
Loop from 1 to n, check which numbers are not in the set. 
Collect missing ones into a result list.
Time: O(n) — one pass to build set, one pass to check
Space: O(n) — set for lookup + result list
