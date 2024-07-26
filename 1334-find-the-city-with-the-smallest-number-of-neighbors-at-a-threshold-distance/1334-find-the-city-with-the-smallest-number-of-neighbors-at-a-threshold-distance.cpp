class Solution {
public:
    int findTheCity(int n, vector<vector<int>>& edges, int distanceThreshold) {
        vector<vector<pair<int,int>>> adj(n);
        vector<vector<int>> shortestPathMatrix(n , vector<int>(n, INT_MAX));

        for (int i = 0; i < n; i ++){
            shortestPathMatrix[i][i] = 0;
        }
        
        for (auto edge : edges){
            int start = edge[0];
            int end = edge[1];
            int weight = edge[2];
            adj[start].emplace_back(end,weight);
            adj[end].emplace_back(start,weight);
        }

        for (int i = 0; i < n; i++){
            dijkstra(n, adj, shortestPathMatrix[i], i);
        }

        return findCity(n, shortestPathMatrix, distanceThreshold);
    }

    void dijkstra (int n, vector<vector<pair<int,int>>>& adj, vector<int>& distances, int source){
        priority_queue< pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>> > pq;
        pq.emplace(0,source);
        fill(distances.begin(), distances.end(), INT_MAX);
        distances[source] = 0;

        while (!pq.empty()){
            auto [currentDistance, currentCity] = pq.top();
            pq.pop();
            if (currentDistance > distances[currentCity]){
                continue;
            }

            for (const auto & [neighbor, edgeWeight] : adj[currentCity]){
                if (distances[neighbor] > currentDistance + edgeWeight) {
                    distances[neighbor] = currentDistance + edgeWeight;
                    pq.emplace(distances[neighbor], neighbor);
                }
            }
        }
    }
    int findCity(int n, const vector<vector<int>>& shortestPathMatrix, int maxdist){
        int fewestCity = -1;
        int fewestReachableCount = n;

        for (int i = 0; i < n; i ++){
            int reachableCount = 0;
            for (int j = 0; j < n; j ++){
                if (i == j){
                    continue;
                }
                if (shortestPathMatrix[i][j] <= maxdist){
                    reachableCount++;
                }
            }
            if (reachableCount <= fewestReachableCount){
                fewestReachableCount = reachableCount;
                fewestCity = i;
            }
        }
        return fewestCity;
    }
};