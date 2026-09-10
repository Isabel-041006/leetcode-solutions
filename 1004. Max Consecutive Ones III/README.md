# 1004. Max Consecutive Ones III

### Difficulty: Medium

## Description
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 
Example 1:


Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:


Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


 
Constraints:


	1 <= nums.length <= 105
	nums[i] is either 0 or 1.
	0 <= k <= nums.length

## Submission Details
- **Status**: Accepted
- **Runtime**: 54
- **Memory**: 22212000
- **Language**: python3

## Code
```python3
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero = 0      # 记录当前窗口内 0 的个数
        left = 0      # 窗口左边界索引
        max_rlt = 0   # 记录历史最大窗口长度

        # i 作为右指针遍历整个数组
        for i in range(len(nums)):
            # 1. 遇到 0，0 的计数器加 1
            if nums[i] == 0:
                zero += 1
            
            # 2. 如果 0 的数量超过了 k，不断右移左指针 left 缩小窗口
            while zero > k:
                if nums[left] == 0:
                    zero -= 1  # 移出窗口的元素如果是 0，计数减 1
                left += 1      # 左指针向右移动
            
            # 3. 此时窗口合法（0 的数量 <= k），更新最大长度
            # 当前窗口长度公式为：右指针 - 左指针 + 1
            max_rlt = max(max_rlt, i - left + 1)

        return max_rlt
```
