// TLE solution -- checks too many times in inner for loop!
class Solution {
public:
  vector<int> maxSlidingWindow(vector<int> &nums, int k) {
    int max_value = 0;

    for (int i = 0; i < k; i++) {
      max_value = std::max(max_value, nums[i]);
    }

    std::vector<int> max_window;
    max_window.push_back(max_value);
    int start = 0;

    for (int r = k; start < nums.size() - k; r++) {
      if (nums[start] == max_value) {
        max_value = INT_MIN;
        for (int i = start + 1; i < start + 1 + k; i++) {
          max_value = std::max(max_value, nums[i]);
        }
      } else {
        max_value = std::max(max_value, nums[r]);
      }
      max_window.push_back(max_value);
      start += 1;
    }
    return max_window;
  }
};

// Optimized solution, O(n)
class Solution {
public:
  vector<int> maxSlidingWindow(vector<int> &nums, int k) {
    std::deque<int> deque_window;

    for (int i = 0; i < k; i++) {
      while (!deque_window.empty() && nums[deque_window.back()] < nums[i])
        deque_window.pop_back();
      deque_window.push_back(i);
    }

    std::vector<int> max_window;
    max_window.push_back(nums[deque_window.front()]);

    for (int r = k; r < nums.size(); r++) {
      if (deque_window.front() <= r - k)
        deque_window.pop_front();

      while (!deque_window.empty() && nums[deque_window.back()] < nums[r])
        deque_window.pop_back();
      deque_window.push_back(r);
      max_window.push_back(nums[deque_window.front()]);
    }
    return max_window;
  }
};
