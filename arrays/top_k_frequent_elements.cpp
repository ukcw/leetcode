class Solution {
public:
  vector<int> topKFrequent(vector<int> &nums, int k) {
    unordered_map<int, int> map;

    for (int n : nums) {
      map[n]++;
    }

    vector<vector<int>> count(nums.size() + 1);

    for (const auto &p : map) {
      count[p.second].push_back(p.first);
    }

    vector<int> result;

    for (int i = count.size() - 1; result.size() < k; i--) {
      for (const auto &num : count[i])
        result.push_back(num);
    }

    return result;
  }
};
