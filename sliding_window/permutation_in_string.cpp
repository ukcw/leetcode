class Solution {
public:
  bool checkInclusion(string s1, string s2) {
    // initialize two arrays of size 26 for both strings to count occurrences
    // check if all chars have the same count, if they do, matches = 26
    // else shift window by 1 to the right then repeat the check
    // if no matches, return false
    if (s1.length() > s2.length())
      return false; // substring does not exist
    int chars_s1[26] = {};
    int chars_s2[26] = {};

    for (int i = 0; i < s1.length(); i++) {
      chars_s1[s1[i] - 'a'] += 1;
      chars_s2[s2[i] - 'a'] += 1;
    }

    int matches = 0;

    for (int i = 0; i < 26; i++) {
      if (chars_s1[i] == chars_s2[i])
        matches += 1;
    }

    if (matches == 26)
      return true;

    for (int i = 0; i < s2.length() - s1.length(); i++) {
      int r = i + s1.length();

      int l_char_idx = s2[i] - 'a';
      chars_s2[l_char_idx] -= 1;
      if (chars_s2[l_char_idx] == chars_s1[l_char_idx]) {
        matches += 1;
      } else if (chars_s2[l_char_idx] + 1 == chars_s1[l_char_idx]) {
        matches -= 1;
      }

      int r_char_idx = s2[r] - 'a';
      chars_s2[r_char_idx] += 1;
      if (chars_s2[r_char_idx] == chars_s1[r_char_idx]) {
        matches += 1;
      } else if (chars_s2[r_char_idx] - 1 == chars_s1[r_char_idx]) {
        matches -= 1;
      }

      if (matches == 26)
        return true;
    }

    return false;
  }
};
