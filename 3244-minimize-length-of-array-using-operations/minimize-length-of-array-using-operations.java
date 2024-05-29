class Solution {
    public int minimumArrayLength(int[] nums) {
        Arrays.sort(nums);
        int n=nums.length;
        int c=1,g=Integer.MAX_VALUE;
        for (int i=1;i<n;i++){
            g=Math.min(g,gcd(nums[i],nums[i-1]));
            if(g<nums[0])return 1;
            if(nums[i]==nums[0])c++;
        }
        int k=(int)Math.ceil(c/(2.0));
        return k;
    }
    private int gcd(int a, int b){
        return b==0?a:gcd(b,a%b);
    }
}