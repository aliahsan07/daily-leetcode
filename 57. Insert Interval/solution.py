class Solution(object):

    def sortedOverlappingIntervals(self, intervals, newInterval):
        self.overlaps = []
        self.output = []
        for interval in intervals:
            if newInterval[0] >= interval[0] and newInterval[0] <= interval[1] or interval[0] >= newInterval[0] and interval[0] <= newInterval[1]:
                self.overlaps.append(interval)
            else:
                self.output.append(interval)

        self.overlaps.sort()
        return (self.overlaps, self.output)

    def mergeInterval(self, interval, newInterval):

        if interval[0] > newInterval[0]:
            return self.mergeInterval(newInterval, interval)

        if newInterval[1] > interval[1]:
            return [interval[0], newInterval[1]]

        return interval

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        overlaps, output = self.sortedOverlappingIntervals(
            intervals, newInterval)

        # loop over intervals
        tempInterval = newInterval
        for interval in overlaps:
            tempInterval = self.mergeInterval(interval, tempInterval)
            # print tempInterval

        output.append(tempInterval)
        output.sort()
        return output
