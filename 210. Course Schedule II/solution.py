class CourseGraph:
    def __init__(self, allCourses, preReqs):

        self.allCourses = allCourses
        self.preReqs = {}
        self.deps = {}

        for course in allCourses:
            self.preReqs[course] = []
            self.deps[course] = []

        for course, preReq in preReqs:
            self.preReqs[course].append(preReq)
            self.deps[preReq].append(course)


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        allCourses = [i for i in range(0, numCourses)]
        if len(prerequisites) == 0:
            return allCourses

        courseGraph = CourseGraph(allCourses, prerequisites)

        order = []

        preReqs = courseGraph.preReqs
        coursesWithNoPreReqs = list(
            filter(lambda node: len(preReqs[node]) == 0, allCourses))

        while coursesWithNoPreReqs:
            course = coursesWithNoPreReqs.pop()
            order.append(course)

            courseDeps = courseGraph.deps[course]

            for c in courseDeps:
                preReqs[c].pop()
                if len(preReqs[c]) == 0:
                    coursesWithNoPreReqs.append(c)

        return order if len(order) == numCourses else []
