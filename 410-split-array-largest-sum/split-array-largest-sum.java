class Solution {
    public int splitArray(int[] nums, int k) {
        int n = nums.length;
        int nums_sum=0, max=Integer.MIN_VALUE;
        for (int num:nums){
            nums_sum+=num;
            max=Math.max(num,max);
        }
        int f=max,l=nums_sum, res=Integer.MAX_VALUE;
        while(f<=l){
            int m=(f+(l-f)/2);
            int sum=0,count=1;
            for(int i=0;i<n;i++)
            {
                if(nums[i]+sum<=m)
                {
                    sum+=nums[i];
                }
                else
                {
                    sum=nums[i];
                    count++;
                }
            }
            if(count<=k)
            {
                res=Math.min(res,m);
                l=m-1;
            }
            else
            {
                f=m+1;
            }
        }
        return res;
    }
}