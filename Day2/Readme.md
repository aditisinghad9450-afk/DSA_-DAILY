DAY 2
1. Largest Number in Array: Find the largest number present in the given array.
   Approach: Start by assuming the first element is the largest. Go through the remaining elements one by one and compare them with the current largest. If a bigger number is found, update the largest value. After checking all the elements, return the largest number.
Time Complexity: O(n)
Space Complexity: O(1)
2. Second Largest Number in Array: Find the second-largest distinct number in the given array.
   Approach: Keep track of the largest and second-largest numbers while traversing the array. If a number greater than the current largest is found, update both variables. Otherwise, if a number is smaller than the largest but greater than the second largest, update the second-largest value. After checking all the elements, return the second-largest distinct number.
Time Complexity: O(n)
Space Complexity: O(1)
3. Reverse Array: Reverse the elements of an array without using another array.
   Approach: Use two pointers, one at the beginning and the other at the end of the array. Swap the elements at these positions and move both pointers towards the middle. Repeat this process until the pointers meet or cross each other.
Time Complexity: O(n)
Space Complexity: O(1)
