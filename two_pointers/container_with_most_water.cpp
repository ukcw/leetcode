class Solution {
public:
  int maxArea(vector<int> &height) {
    int l = 0, r = height.size() - 1;
    int greatestArea = 0;

    while (l < r) {
      greatestArea =
          std::max(greatestArea, (r - l) * std::min(height[l], height[r]));
      height[l] < height[r] ? l++ : r--;
    }

    return greatestArea;
  }
};
