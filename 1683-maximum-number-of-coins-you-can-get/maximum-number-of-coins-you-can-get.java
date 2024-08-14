class Solution {
    public int maxCoins(int[] piles) {
        int n=piles.length/3;
        Arrays.sort(piles);
        int sum=0;
        for (int i=n;i<3*n;i=i+2){
            sum+=piles[i];
        }
        return sum;
    }
}