class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = [i for i in range(len(isConnected))]
        rank = [1] * len(isConnected)
        provinces = len(isConnected)

        def find(v):
            while v != parent[v]:
                v = parent[v]
            return v

        def union(v1, v2):
            v1 = find(v1)
            v2 = find(v2)

            if v1 == v2:
                return 0

            if rank[v1] >= rank[v2]:
                parent[v2] = v1
                rank[v1] += 1
            else:
                parent[v1] = v2
                rank[v2] += 1

            return 1

        for idxLst, lst in enumerate(isConnected):
            for idxCity, city in enumerate(lst):
                if idxCity >= idxLst and city == 1:
                    provinces -= union(idxLst, idxCity)
        return provinces
