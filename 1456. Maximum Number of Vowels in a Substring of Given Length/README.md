# 1456. Maximum Number of Vowels in a Substring of Given Length

### Difficulty: Medium

## Description
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 
Example 1:


Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.


Example 2:


Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.


Example 3:


Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.


 
Constraints:


	1 <= s.length <= 105
	s consists of lowercase English letters.
	1 <= k <= s.length

## Submission Details
- **Status**: Accepted
- **Runtime**: 71
- **Memory**: 19940000
- **Language**: python3

## Code
```python3
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        current_vow = sum(1 for i in range(k) if s[i] in vowels)
        max_vow = current_vow

        left = 0
        right = k - 1

        while right < len(s) - 1:  
            if s[left] in vowels:
                current_vow -= 1
      
            left += 1
            right += 1

            if s[right] in vowels:
                current_vow += 1

            max_vow = max(max_vow, current_vow)

        return max_vow
```
