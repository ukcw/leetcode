class Solution {
public:
  vector<int> dailyTemperatures(vector<int> &temperatures) {
    std::stack<std::pair<int, int>> temps;
    std::vector<int> answer(temperatures.size());

    for (int i = 0; i < temperatures.size(); i++) {
      while (!temps.empty() && temps.top().first < temperatures[i]) {
        int value = i - temps.top().second;
        answer[temps.top().second] = value;
        temps.pop();
      }
      temps.push({temperatures[i], i});
    }

    return answer;
  }
};
