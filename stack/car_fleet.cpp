class Solution {
public:
  int carFleet(int target, vector<int> &position, vector<int> &speed) {
    // for a car to not bump into a car that is ahead of it
    // this condition has to hold:
    //              speed[car behind] <= speed[car in front]
    std::vector<std::pair<int, int>> cars;

    for (int i = 0; i < position.size(); i++) {
      cars.push_back({position[i], speed[i]});
    }

    std::sort(cars.begin(), cars.end(),
              [](const std::pair<int, int> &a, const std::pair<int, int> &b) {
                return a.first < b.first;
              });

    std::stack<float> time_taken;

    for (const auto &car : cars) {
      float time = (float)(target - car.first) / car.second;
      if (time_taken.empty()) {
        time_taken.push(time);
      } else {
        while (!time_taken.empty() && time_taken.top() <= time) {
          time_taken.pop();
        }
        time_taken.push(time);
      }
    }

    return time_taken.size();
  }
};
