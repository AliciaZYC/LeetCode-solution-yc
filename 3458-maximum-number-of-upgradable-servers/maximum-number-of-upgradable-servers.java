class Solution {
    public int[] maxUpgrades(int[] count, int[] upgrade, int[] sell, int[] money) {
        int n = count.length;
        int[] result = new int[n];
        for(int i = 0;i<n;i++){
            result[i] = Math.min(count[i], (int)((money[i]+(long)sell[i]*count[i])/((long)upgrade[i]+sell[i])));
        }
        return result;
    }
}