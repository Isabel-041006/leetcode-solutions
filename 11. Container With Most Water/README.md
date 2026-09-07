# 11. Container With Most Water

### Difficulty: Medium

## Description
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 
Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


Example 2:


Input: height = [1,1]
Output: 1


 
Constraints:


	n == height.length
	2 <= n <= 105
	0 <= height[i] <= 104

## Submission Details
- **Status**: Accepted
- **Runtime**: 61
- **Memory**: 29508000
- **Language**: python3

## Code
```python3
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_water = 0

        while l < r:
            current_water = (r - l) * min(height[l], height[r])
            max_water = max(max_water, current_water)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_water
```
