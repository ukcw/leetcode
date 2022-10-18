# DFS Solution
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return True

        numberOfRooms = len(rooms)
        visit = set()
        adjList = {}

        for idx, roomKeys in enumerate(rooms):
            adjList[idx] = roomKeys

        def dfs(room):
            if room in visit:
                return
            visit.add(room)
            for roomKey in adjList[room]:
                dfs(roomKey)

        dfs(0)
        return len(visit) == numberOfRooms
