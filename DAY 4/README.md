#Running Sum of 1d Array 

Approach: Walk the array once, keeping a running total.
At each index, add the current element to the total and append it to a result list.
Time: O(n) — single pass
Space: O(n) — result list

#Max Consecutive Ones 

Approach: Walk the array once with two variables: current streak and best streak. 
When you see a 1, grow the current streak.
When you see a 0, compare current to best, update best if needed, reset current to 0. 
After the loop, compare one final time.
Time: O(n) — single pass
Space: O(1) — two variables

#Best Time to Buy and Sell Stock 

Approach: Walk the array once, tracking the minimum price seen so far.
At each step, compute profit as current price minus min price. 
If that beats the best profit, update it.
Two independent checks per step: one for new minimum, one for new best profit.
Time: O(n) — single pass
Space: O(1) — two variables
