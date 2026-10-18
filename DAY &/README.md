#DAY 7

Problem 1: Rotate Array 

Rotate array to the right by k positions, in-place
Approach: Three reverses, reverse whole array, reverse first k, reverse rest
Key idea: k = k % len(nums) to handle k > array length
Helper function reverses a portion using two pointers walking inward
Time: O(n), Space: O(1)

Problem 2: Left Rotation

Rotate array to the left by k positions, in-place
Same three-reverse approach, different order: reverse first k, reverse rest, reverse whole array
Time: O(n), Space: O(1)

Problem 3: Reverse Array in Groups 

Reverse every group of k elements; last group may be smaller
Reuse the same reverse helper from Problem 1
Outer loop jumps by k: for i in range(0, len(arr), k)
Each chunk: left = i, right = min(i + k - 1, len(arr) - 1)
Time: O(n), Space: O(1)
