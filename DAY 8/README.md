#Day 8 

#Problem 1: Valid Palindrome 
Check if a string reads the same forward and backward, ignoring non-alphanumeric characters and case
Two pointers from ends, skip non-alphanumeric with .isalnum(), compare with .lower()
If mismatch found, return False immediately; if loop finishes, return True
Time: O(n), Space: O(1)

#Problem 2: Reverse String 
Reverse a list of characters in-place
Two pointers: swap s[left] and s[right], walk inward
Time: O(n), Space: O(1)

#Problem 3: Reverse Vowels of a String
Swap only vowels, leave other characters in place
Two pointers from ends: skip non-vowels on each side, swap when both are vowels
Check vowels with s[i].lower() not in 'aeiou'
Strings are immutable in Python, convert to list first, join back at the end
Time: O(n), Space: O(n) for the list conversion
