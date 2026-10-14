def countFrequencies(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    return freq
