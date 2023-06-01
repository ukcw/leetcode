class Solution {
public:
  int evalRPN(vector<string> &tokens) {
    std::stack<int> s;

    for (std::string c : tokens) {
      if (c != "+" && c != "-" && c != "*" && c != "/") {
        s.push(std::stoi(c));
      } else {
        int num2 = s.top();
        s.pop();
        int num1 = s.top();
        s.pop();
        int result = applyOp(c, num1, num2);
        s.push(result);
      }
    }

    return s.top();
  }

  int applyOp(std::string op, int num1, int num2) {
    return op == "+"   ? num1 + num2
           : op == "-" ? num1 - num2
           : op == "*" ? num1 * num2
                       : num1 / num2;
  }
};
