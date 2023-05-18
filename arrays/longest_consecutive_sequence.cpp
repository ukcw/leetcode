class Solution {
public:
  int longestConsecutive(vector<int> &nums) {
    std::set<int> num_set(nums.begin(), nums.end());
    int global_best{0};

    for (int i : num_set) {
      if (num_set.count(i - 1) != 1) {
        int local_best = 1;
        while (num_set.count(i + 1) == 1) {
          local_best += 1;
          i += 1;
        }
        global_best = std::max(global_best, local_best);
      }
    }
    return global_best;
  }
};
