class Solution {
    public long minimumCost(int[] nums) {
        int n=nums.length;
        Arrays.sort(nums);
        int medium=nums[n/2],inc=medium,dec=medium;
        while(!isPalidrome(inc))inc++;
        while(!isPalidrome(dec))dec--;
        return Math.min(cost(nums,inc),cost(nums,dec));
    }
    public boolean isPalidrome(int n){
        int r,sum=0,tmp;
        tmp=n;
        while(n>0){
            r=n%10;
            sum=(sum*10)+r;
            n=n/10;
        }
        return tmp==sum;
    }
    public long cost(int[] nums,int r){
        long cost=0;
        for(int n:nums)cost+=Math.abs(n-r);
        return cost;
    }
}