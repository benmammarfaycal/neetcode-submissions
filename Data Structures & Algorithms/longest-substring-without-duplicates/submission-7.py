class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        maxi = 0

        for right, ch in enumerate(s):
            if ch in char_index and char_index[ch] >= left:
                left = char_index[ch] + 1

            char_index[ch] = right
            maxi = max(maxi, right - left + 1)

        return maxi