class Solution {
public:
  vector<int> twoSum(vector<int> &nums, int target) {
    unordered_map<int, int> seen;

    for (int i = 0; i < nums.size(); i++) {
      int other = target - nums[i];

      if (seen.find(other) != seen.end()) {
        return {seen[other], i};
      } else {
        seen[nums[i]] = i;
      }
    }

    return {};
  }
};
