class Solution(object):
    def rob(self, nums):
        size = len(nums)
        if size == 0:
            return 0
        if size == 1:
            return nums[0]
        left = self.execution(nums[0:-1], size-1)
        right = self.execution(nums[1:], size-1)
        return max(left, right)

    def execution(self, nums, size):
        """
        :type nums: List[int]
        :rtype: int
        """

        if size <= 2:
            return max(nums)

        dp = [0 for i in range(size)]
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[2] + nums[0]

        for i in range(3, size):

            if dp[i-2] >= dp[i-3]:
                dp[i] = nums[i] + dp[i-2]
            else:
                dp[i] = nums[i] + dp[i-3]

        return max(dp[size-1], dp[size-2])
