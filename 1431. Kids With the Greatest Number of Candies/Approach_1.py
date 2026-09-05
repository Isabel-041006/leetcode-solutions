class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        rlt = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                rlt.append(True)
            else:
                rlt.append(False)
        return rlt