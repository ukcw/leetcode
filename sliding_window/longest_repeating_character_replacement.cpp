class Solution {
public:
  int characterReplacement(string s, int k) {
    int chars[26] = {};
    int longest_length = 0;
    int substring_start = 0;
    for (int j = 0; j < s.length(); j++) {
      chars[s[j] - 65] += 1;
      while (j - substring_start + 1 - *std::max_element(chars, chars + 26) >
             k) {
        chars[s[substring_start] - 65] -= 1;
        substring_start += 1;
      }
      longest_length = std::max(longest_length, j - substring_start + 1);
    }
    return longest_length;
  }
};
