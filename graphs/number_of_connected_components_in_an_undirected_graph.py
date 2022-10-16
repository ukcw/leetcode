class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

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

            return 1  # found a new merge so subtract 1 less non-connected component

        components = n
        for start, end in edges:
            components -= union(start, end)

        return components
