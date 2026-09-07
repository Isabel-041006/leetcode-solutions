class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        oper = 0

        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == k:
                oper += 1
                left += 1
                right -= 1
            elif current_sum > k:
                right -= 1
            else:
                left +=1
        return oper