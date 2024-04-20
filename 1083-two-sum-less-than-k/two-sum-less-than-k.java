class Solution {
    public int twoSumLessThanK(int[] nums, int k) {
        Arrays.sort(nums);
        int left=0, right=nums.length-1;
        int res=-1;
        while(left<right){
            if (nums[left]>k/2)break;
            int sum=nums[left]+nums[right];
            if(sum<k){
                res=Math.max(res,sum);
                left++;
            }else right--;
        }
        return res;
    }
}