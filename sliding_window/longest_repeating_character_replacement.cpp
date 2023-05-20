class Solution {
public:
  int characterReplacement(string s, int k) {
    int chars[26] = {};
    int longest_length = 0;
    int substring_start = 0;
    for (int j = 0; j < s.length(); j++) {
      chars[s[j] - 65] += 1;
      // using a while loop here provides no benefits as we can not care
      // about an invalid window that is of the same size as the max length
      // we have currently found. the window size will only extend if we find
      // another valid window that is longer than the current one!
      if (j - substring_start + 1 - *std::max_element(chars, chars + 26) > k) {
        chars[s[substring_start] - 65] -= 1;
        substring_start += 1;
      }
      longest_length = std::max(longest_length, j - substring_start + 1);
    }
    return longest_length;
  }
};
