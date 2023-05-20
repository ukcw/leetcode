class Solution {
public:
  int maxProfit(vector<int> &prices) {
    int min_price = INT_MAX;
    int max_profit = 0;

    for (int i = 0; i < prices.size(); i++) {
      max_profit = std::max(max_profit, prices[i] - min_price);
      min_price = std::min(min_price, prices[i]);
    }

    return max_profit;
  }
};
