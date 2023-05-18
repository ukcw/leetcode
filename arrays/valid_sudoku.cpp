class Solution {
public:
  bool isValidVec(const vector<char> &vec) {
    std::set<char> seen;

    for (char c : vec) {
      if (c != '.' && seen.count(c) > 0) {
        return false;
      }
      seen.insert(c);
    }

    return true;
  }

  bool isValidSudoku(vector<vector<char>> &board) {
    std::unordered_map<int, std::vector<char>> grids;
    std::unordered_map<int, std::vector<char>> columns;

    for (int i = 0; i < board.size(); i++) {
      if (!isValidVec(board[i])) {
        return false;
      }
      for (int j = 0; j < board[0].size(); j++) {
        grids[i / 3 * 3 + j / 3].push_back(board[i][j]);
        columns[j].push_back(board[i][j]);
      }
    }

    for (const auto &grid : grids) {
      if (!isValidVec(grid.second)) {
        return false;
      }
    }

    for (const auto &col : columns) {
      if (!isValidVec(col.second)) {
        return false;
      }
    }

    return true;
  }
};
