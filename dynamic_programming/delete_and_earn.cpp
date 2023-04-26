#include <iostream>
#include <map>
#include <vector>
class Solution {
public:
  int deleteAndEarn(std::vector<int> &nums) {
    // collect into dictionary vals and counts
    std::map<int, int> counts;

    for (int num : nums) {
      counts[num] += num;
    }

    std::sort(nums.begin(), nums.end());

    // remove duplicates in place
    std::vector<int>::iterator it = std::unique(nums.begin(), nums.end());
    nums.erase(it, nums.end());

    std::vector<int> dp(nums.size());

    int i = 0;

    // iterate over unique array of sorted nums
    for (const int &num : nums) {
      if (i == 0) {
        dp[0] = counts[num];
      } else if (i == 1) {
        dp[1] = nums[0] == nums[1] - 1 ? std::max(dp[0], counts[num])
                                       : counts[num] + dp[0];
      } else {
        dp[i] = nums[i - 1] == nums[i] - 1
                    ? std::max(counts[num] + dp[i - 2], dp[i - 1])
                    : counts[num] + std::max(dp[i - 1], dp[i - 2]);
      }
      i++;
    }

    // return dp answer
    return dp.back();
  }
};
