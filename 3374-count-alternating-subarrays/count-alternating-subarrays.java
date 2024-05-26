class Solution {
    public long countAlternatingSubarrays(int[] nums) {
        long res=0l;
        int n=nums.length;
        int i=0,j=1;
        while(j<n){
            if(nums[j]==nums[j-1]){
                i=j;
            }else{
                res+=(j-i);
            }
            j++;
        }
        return res+n;
    }
}