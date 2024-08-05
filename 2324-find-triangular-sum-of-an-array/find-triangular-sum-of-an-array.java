class Solution {
    // public int triangularSum(int[] nums) {
    //     int l=nums.length;
    //     int sum=0;
    //     for (int i=0;i<l;i++){
    //         sum+=Combination(l-1,i)*nums[i];
    //     }
    //     return sum%10;
    // }
    // public static int Combination(int n,int k){
    //     int a=1,b=1;
    //     if(k>n/2)k=n-k;
    //     for(int i=1;i<=k;i++){
    //         a*=(n+1-i);
    //         b*=i;
    //     }
    //     return a/b;
    // }
    public int triangularSum(int[] nums) {
        int l = nums.length;
        int sum = 0;
        
        while (l > 1) {
            for (int i = 0; i < l - 1; i++) {
                nums[i] = (nums[i] + nums[i + 1]) % 10;
            }
            l--;
        }
        
        return nums[0];
    }
}