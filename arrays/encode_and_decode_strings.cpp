class Codec {
public:
  // Encodes a list of strings to a single string.
  string encode(vector<string> &strs) {
    std::stringstream s;
    for (const std::string &str : strs) {
      s << str.length() << '#' << str;
    }
    std::string s_out = s.str();
    return s_out;
  }

  // Decodes a single string to a list of strings.
  vector<string> decode(string s) {
    std::vector<std::string> strs;

    int i = 0;

    while (i < s.length()) {
      std::string word_length = "";
      while (s[i] != '#') {
        word_length.push_back(s[i]);
        i++;
      }
      int substr_length = std::stoi(word_length);
      std::string substr = s.substr(i + 1, substr_length);
      strs.push_back(substr);
      i += substr_length + 1;
    }

    return strs;
  }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));
