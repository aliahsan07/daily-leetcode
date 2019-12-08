from collections import deque
import math

class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        
        ans = 0
        while Y > X:
            ans += 1
            if Y%2: Y += 1
            else: Y /= 2

        return ans + X-Y
