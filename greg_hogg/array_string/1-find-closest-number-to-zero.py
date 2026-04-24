class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for x in nums:
            if abs(x) < abs(closest):
                closest = x 
                # we can return this directly closest abs value. but if there is, like -1, -1 exist and no positive 1, we need to return -1, if we return abs(-1) (output 1) will be wrong.

        # For that we need to check if there is positive 1 availabe or not, if availabe we just can return abs(x), if not we need to return the excat number, which is maybe -1
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest
# Time: O(n)
# Space O(1)