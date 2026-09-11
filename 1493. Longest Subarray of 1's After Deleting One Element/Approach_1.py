class Solution:

  def longestSubarray(self, nums: list[int]) -> int:
    left = 0
    zero_count = 0
    max_len = 0

    for right in range(len(nums)):
      # 如果当前遇到 0，0 的计数加 1
      if nums[right] == 0:
        zero_count += 1

      # 当窗口内 0 的数量超过 1 时，收缩左边界，直到 0 的数量 <= 1
      while zero_count > 1:
        if nums[left] == 0:
          zero_count -= 1
        left += 1

      # 窗口大小为 (right - left + 1)，扣除必须删除的 1 个元素后，长度为 (right - left)
      max_len = max(max_len, right - left)

    return max_len