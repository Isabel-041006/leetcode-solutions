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