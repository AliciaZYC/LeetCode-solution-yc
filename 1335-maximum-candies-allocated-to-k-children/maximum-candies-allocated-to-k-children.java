class Solution {
    public int maximumCandies(int[] candies, long k) {
        int left=0,right=10000000;
        while(left<right){
            long sum=0;
            int mid=(left+right+1)/2;
            for(int a:candies){
                sum+=a/mid;
            }
            if(k>sum) right=mid-1;
            else left=mid;
        }
        return left;
    }
}