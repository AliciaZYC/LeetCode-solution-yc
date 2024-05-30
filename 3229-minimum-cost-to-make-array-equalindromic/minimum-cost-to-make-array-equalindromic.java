class Solution {
    public long minimumCost(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);
        int mid = nums[n/2];
        int in = mid;
        int dc = mid;
        while(!isPal(in)) in++;
        while(!isPal(dc)) dc--;
        return Math.min(calculateCost(nums,in),calculateCost(nums,dc));

    }
    public boolean isPal(int n){
        int r, s = 0, temp;
        temp = n;
        while(n>0){
            r = n % 10;
            s = (s * 10) + r;
            n /= 10;
        }
        return temp == s;
    }
    public long calculateCost(int [] nums, int r){
        long cost = 0;
        for(int n : nums) cost += Math.abs(n-r);
        return cost;
    }
}