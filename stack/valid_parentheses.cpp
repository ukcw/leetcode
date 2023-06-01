class Solution {
public:
  bool isValid(string s) {
    std::stack<char> paren_stack;

    std::unordered_map<char, char> brackets = {
        {')', '('}, {'}', '{'}, {']', '['}};

    for (char b : s) {
      if (brackets.count(b) > 0) {
        if (!paren_stack.empty() && paren_stack.top() == brackets[b]) {
          paren_stack.pop();
        } else {
          return false;
        }
      } else {
        paren_stack.push(b);
      }
    }
    return paren_stack.empty();
  }
};
