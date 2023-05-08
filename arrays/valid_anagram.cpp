class Solution {
public:
  bool isAnagram(string s, string t) {

    if (s.length() != t.length())
      return false;

    std::unordered_map<char, int> dic;
    int n = s.length();

    for (int i = 0; i < n; i++) {
      dic[s[i]]++;
      dic[t[i]]--;
    }

    for (const auto &[key, value] : dic) {
      if (value != 0) {
        return false;
      }
    }
    return true;
  }
};
