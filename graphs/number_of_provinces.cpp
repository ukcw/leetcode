class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        
        int parent[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        } 

        int rank[n];
        for (int i = 0; i < n; i++) {
            rank[i] = 1;
        }
        
        int provinces = isConnected.size();
        for (int i = 0; i < isConnected.size(); i++) {
            for (int j = i; j < isConnected.size(); j++) {
                if (isConnected[i][j] == 1) {
                    provinces -= unionF(i, j, parent, rank);
                }
            }
        }
        
        return provinces;
    }

private:
    int find(int v, int parent[]) {
        while (v != parent[v]) {
            v = parent[v];
        }
        return v;
    }

    int unionF(int v1, int v2, int parent[], int rank[]) {
        v1 = find(v1, parent);
        v2 = find(v2, parent);

        if (v1 == v2) return 0;
    
        if (rank[v1] >= rank[v2]) {
            parent[v2] = v1;
            rank[v1] += 1;
        } else {
            parent[v1] = v2;
            rank[v2] += 1;
        }
        
        return 1;
    }
};
