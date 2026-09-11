# 1493. Longest Subarray of 1's After Deleting One Element

### Difficulty: Medium

## Description
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 
Example 1:


Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.


Example 2:


Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].


Example 3:


Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.


 
Constraints:


	1 <= nums.length <= 105
	nums[i] is either 0 or 1.

## Submission Details
- **Status**: Accepted
- **Runtime**: 44
- **Memory**: 24360000
- **Language**: python3

## Code
```python3
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
```
