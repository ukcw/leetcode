class Solution {
public:
  string minWindow(string s, string t) {
    // length of t must be greater than or equal to s
    if (t.length() > s.length())
      return "";

    std::unordered_map<char, int> counts;
    for (char c : t) {
      counts[c] += 1;
    }
    int leftover = counts.size();

    // loop:
    // search until chars in t are found
    // shorten window from left until it is invalid
    // re-search from right until a match is found again
    int start = 0;
    int substr_start = 0, substr_end = 0;

    for (int j = 0; j < s.length(); j++) {
      if (counts.count(s[j]) > 0) {
        counts[s[j]] -= 1;
        if (counts[s[j]] == 0) {
          leftover -= 1;
          while (start <= j && leftover == 0) {
            if (counts.count(s[start]) > 0) {
              counts[s[start]] += 1;
              if (counts[s[start]] == 1) {
                leftover += 1;
              }
            }
            if (substr_end - substr_start == 0 ||
                substr_end - substr_start > j - start + 1) {
              substr_start = start;
              substr_end = j + 1;
            }
            start += 1;
          }
        }
      }
    }
    return s.substr(substr_start, substr_end - substr_start);
  }
};
