import collections


class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        count = collections.Counter(nums)
        keys = sorted(count.keys())

        for key in keys:
            if count[key] > 0:
                minus = count[key]
                for i in range(key, key+k):
                    if count[k] < minus:
                        return False
                    count[k] -= minus

        return True
