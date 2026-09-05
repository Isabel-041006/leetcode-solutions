class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        rlt = []
        max_candies = max(candies)

        for i in candies:
            if i + extraCandies >= max_candies:
                rlt.append(True)
            else:
                rlt.append(False)
        return rlt