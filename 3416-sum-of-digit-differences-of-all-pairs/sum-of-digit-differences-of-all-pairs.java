class Solution {
    public long sumDigitDifferences(int[] nums) {
        int n=nums.length,m=String.valueOf(nums[0]).length();
        int [][] count=new int[m][10];
        long res=1L * n * (n - 1) / 2 * m;
        for (int a : nums) {
            for (int i = 0; i < m && a > 0; i++) {
                res -= count[i][a % 10]++;
                a /= 10;
            }
        }
        return res;
        }
}