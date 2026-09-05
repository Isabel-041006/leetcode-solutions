# 345. Reverse Vowels of a String

### Difficulty: Easy

## Description
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 
Example 1:


Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".


Example 2:


Input: s = "leetcode"

Output: "leotcede"


 
Constraints:


	1 <= s.length <= 3 * 105
	s consist of printable ASCII characters.

## Submission Details
- **Status**: Accepted
- **Runtime**: 9
- **Memory**: 20480000
- **Language**: python3

## Code
```python3
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = set("aeiouAEIOU")
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            s[left] , s[right] = s[right] , s[left]
            left += 1
            right -= 1
        return "".join(s)
```
