from collections import defaultdict


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        sumCounter = defaultdict(int)
        sumCounter[0] = 1
        count = 0

        sum = 0
        for num in nums:

            sum += num
            if sum - k in sumCounter:
                count += (sumCounter[sum - k])
            sumCounter[sum] += 1

        return count
