DAY 1-
1. Two Sum
Problem: Given an array and a target, find the indices of two numbers that add up to the target.
Approach: Use two loops to check every possible pair. If the sum of two numbers equals the target, return their indices.
Time Complexity: O(n²)
Space Complexity: O(1)
2. Contains Duplicate
Problem: Check if any number appears more than once in the array.
Approach: Use two loops to compare each element with the elements that come after it. If any two elements are equal, return true. If no duplicates are found, return false.
Time Complexity: O(n²)
Space Complexity: O(1)
3. Single Number
Problem: Every number appears twice except one. Find the number that appears only once.
Approach: For each element, compare it with every other element in the array. If the same number is found elsewhere, mark it as not unique and move to the next element. If no match is found, return that number.
Time Complexity: O(n²)
Space Complexity: O(1)
