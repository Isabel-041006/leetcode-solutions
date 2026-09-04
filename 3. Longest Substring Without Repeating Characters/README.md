# 3. Longest Substring Without Repeating Characters

### Difficulty: Medium

## Description
Given a string s, find the length of the longest substring without duplicate characters.

 
Example 1:


Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.


Example 2:


Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.


Example 3:


Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


 
Constraints:


	0 <= s.length <= 105
	s consists of English letters, digits, symbols and spaces.

## Submission Details
- **Status**: Accepted
- **Runtime**: 416
- **Memory**: 16804000
- **Language**: python

## Code
```python
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
```
