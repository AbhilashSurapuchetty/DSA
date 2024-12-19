class Solution {
    public int maxProfit(int[] prices) {
        int v = prices.length;
        int s = prices[0];
        int result = 0;

        for (int i=1 ; i < v;i++) {
            if (s < prices[i]) {
                result = result + prices[i] - s;

            }
            s = prices[i];

        }
        return result;


        
    }
}