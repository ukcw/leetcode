class Solution {
public:
  void helper(vector<string> &parentheses, int max_length,
              std::string candidate, int l_count, int r_count) {
    if (candidate.length() == max_length * 2) {
      parentheses.push_back(candidate);
    }
    if (l_count < max_length) {
      candidate += '(';
      helper(parentheses, max_length, candidate, l_count + 1, r_count);
      candidate.pop_back();
    }
    if (r_count < l_count) {
      candidate += ')';
      helper(parentheses, max_length, candidate, l_count, r_count + 1);
      candidate.pop_back();
    }
  }

  vector<string> generateParenthesis(int n) {
    // at each stage, we can add a
    // left parenthesis: only if we have not exceeded length n * 2
    // right parenthesis: only if we have num(left parenthesis) > num(right
    // parenthesis)
    vector<string> parentheses;

    helper(parentheses, n, "", 0, 0);
    return parentheses;
  }
};
