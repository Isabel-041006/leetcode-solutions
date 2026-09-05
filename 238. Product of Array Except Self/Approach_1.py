class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        right = 1
        for i in range(n):
            answer[i] = right
            right *= nums[i]

        left = 1
        for j in range(n-1,-1,-1):
            answer[j] *= left
            left *= nums[j]
        return answer