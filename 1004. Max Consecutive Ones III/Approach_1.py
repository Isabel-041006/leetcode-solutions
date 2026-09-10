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