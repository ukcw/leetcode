class Solution {
public:
  bool containsDuplicate(vector<int> &nums) {
    return std::set<int>(nums.begin(), nums.end()).size() < nums.size();
  }
};
