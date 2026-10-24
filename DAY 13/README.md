#DAY 13

#Problem 1: Contains Duplicate II

Use a set as a sliding window of size k
Loop through array: if element already in set → return True
Add element to set
If i >= k: remove nums[i-k] to keep window size
Time: O(n) 
Space: O(k)

#Problem 2: Find All Anagrams in a String 

Build p_count dict for pattern p
Build w_count dict for first window of size len(p) in s
If dicts match → append index 0 to result
Slide: add new char, remove old char (delete key if count hits 0)
If dicts match → append i - len(p) + 1 to result
Time: O(n) 
Space: O(1) — at most 26 letters

#Problem 3: Permutation in String

Nearly identical to Find All Anagrams
Same sliding window + dict comparison
Instead of collecting indices, return True on first match
Return False if no window matches
Time: O(n) 
Space: O(1)
