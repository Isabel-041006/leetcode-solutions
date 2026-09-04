class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l_s = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in l_s:
                l_s.remove(s[left])
                left += 1
            l_s.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len