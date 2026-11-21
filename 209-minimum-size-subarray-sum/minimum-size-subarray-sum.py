class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        total = 0
        mini = float('inf')
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                mini = min(mini, right - left + 1)
                total -= nums[left]
                left += 1
        if mini == float('inf'):
            return 0
        return mini