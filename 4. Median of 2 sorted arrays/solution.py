from decimal import Decimal


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        if len(nums2) < len(nums1):
            return self.findMedianSortedArrays(nums2, nums1)

        length1 = len(nums1)
        length2 = len(nums2)
        totalLength = length1 + length2

        medianIndex = (totalLength + 1) // 2

        lo = 0
        hi = length1
        while lo <= hi:

            partitionX = (lo + hi) // 2
            partitionY = medianIndex - partitionX
            maxLeftX = Decimal(
                '-Infinity') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = Decimal(
                'Infinity') if partitionX == length1 else nums1[partitionX]

            maxLeftY = Decimal(
                '-Infinity') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = Decimal(
                'Infinity') if partitionY == length2 else nums2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # found the right partitions

                if totalLength % 2 == 0:
                    return ((max(maxLeftX, maxLeftY) + min(minRightX, minRightY)))/2.0
                return max(maxLeftX, maxLeftY)

            elif maxLeftX > minRightY:
                # move back
                hi = partitionX - 1
            else:
                # move ahead
                lo = partitionX + 1

        return
