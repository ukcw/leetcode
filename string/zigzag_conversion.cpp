#include<iostream>
#include<vector>
#include<string>

using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1 || numRows >= s.length()) return s;

        vector<string> res (numRows, "");
        int rowIndex = 0;
        int step = 1;

        for (char const &letter : s) {
            if (rowIndex == 0) 
                step = 1;
            if (rowIndex == numRows - 1) 
                step = -1;

            res[rowIndex] += letter;
            rowIndex += step;
        }

        string output;
        for (auto &str : res) 
            output += str;
        
        return output;
    }
};

int main() {
    Solution sol = Solution();
    cout << sol.convert("PAYPALISHIRING", 3) << endl;
}
