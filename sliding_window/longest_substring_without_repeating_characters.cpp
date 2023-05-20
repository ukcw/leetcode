class Solution {
public:
  int lengthOfLongestSubstring(string s) {
    int substring_start = 0, longest_length = 0;
    std::unordered_map<char, int> char_position;
    for (int i = 0; i < s.length(); i++) {
      if (char_position.count(s[i]) > 0) {
        substring_start = char_position[s[i]] + 1 > substring_start
                              ? char_position[s[i]] + 1
                              : substring_start;
      }
      char_position[s[i]] = i;
      longest_length = std::max(longest_length, i - substring_start + 1);
    }
    return longest_length;
  }
};
