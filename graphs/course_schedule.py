class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodes = {}

        # we first create a dictionary of lists
        # each lists tells us the prerequisites for a given course
        # for example, if we have prerequisites = [[1,0]]
        # then our dictionary = { 0: [], 1: [0] }

        for course, prereq in prerequisites:
            if course not in nodes:
                nodes[course] = []

            if prereq not in nodes:
                nodes[prereq] = []

            nodes[course].append(prereq)

        # how do we know if a course (key) in our dictionary can be taken?
        # if the course's value is an empty list []
        # for courses that begin with a list of prerequisites, we want to
        # determine that the list of prerequisites can also be taken.
        # as such, we design a recursive procedure that uses DFS to check
        # that the ending point of a list of prerequisites can be taken.

        # an important note to make here is the fact that recursively going
        # through the list of prerequisites mean that once we have determined
        # that a course (or prerequisite) can be taken, we do not have to ever
        # check again --> as such, we remove the prerequisite from list of
        # prerequisites for a course (it is as if the prerequisite does not
        # exist)

        def isCompleteable(node, visited):
            if node in visited:
                return False

            if not nodes[node]:
                return True

            visited.add(node)
            while nodes[node]:
                if isCompleteable(nodes[node][0], visited):
                    nodes[node].remove(nodes[node][0])
                else:
                    return False
            visited.remove(node)

            return True

        for node in list(nodes.keys()):
            if not isCompleteable(node, set()):
                return False

        return True
