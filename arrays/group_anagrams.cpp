class Solution {
public:
  vector<vector<string>> groupAnagrams(vector<string> &strs) {
    unordered_map<string, vector<string>> anagrams;

    for (auto s : strs) {
      string sortedString = s;
      sort(sortedString.begin(), sortedString.end());

      anagrams[sortedString].push_back(s);
    }

    vector<vector<string>> result;

    for (auto &pair : anagrams) {
      result.push_back(pair.second);
    }

    return result;
  }
};
