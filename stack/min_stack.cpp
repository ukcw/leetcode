class MinStack {
public:
  std::vector<std::pair<int, int>> vec;

  MinStack() {}

  void push(int val) {
    vec.empty() ? vec.push_back({val, val})
                : vec.push_back({val, std::min(vec.back().second, val)});
  }

  void pop() { vec.pop_back(); }

  int top() { return vec.back().first; }

  int getMin() { return vec.back().second; }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
