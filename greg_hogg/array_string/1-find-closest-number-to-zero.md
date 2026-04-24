# Find closest number to zero

Algomap: https://algomap.io/problems/find-closest-number-to-zero

Leetcode: https://leetcode.com/problems/find-closest-number-to-zero/description/

Note:
Which number is closest to zero? -4 or -2

To see which number is closest to 0, compare their absolute values:

```text
∣−4∣=4

∣−2∣=2
```
Since 2 < 4, -2 is closer to 0.


#### Problem:
Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.

 Sample Input:

Input: nums = [-4,-2,1,4,8]

Output: 1

💡 Step-by-Step Thought Process-

1. Initialize a variable closest to the first number in the list (-4 in this case).
2. Loop through each number in the array.
3. Compare the absolute value of the current number to the absolute value of closest.
4. If it’s closer to zero, update closest.
5. If there are two numbers equally as close, choose the positive one.

```py
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for x in nums:
            if abs(x) < abs(closest):
                closest = x 
        # Step 5:
        if closest < 0 and abs(closest) in nums: 
            return abs(closest)
        else:
            return closest
# Time: O(n)
# Space O(1)
```