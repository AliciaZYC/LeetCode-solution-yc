class Solution {
    public int splitArray(int[] nums, int k) {
        int high = 0;
        int low = 0;
        for (int num : nums) {
            high += num;
            if (num > low) low = num;
        }

        while (low <= high) {
            int mid = low + (high - low)/2;
            if (check(nums, mid) <= k) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    int check(int[] nums, int maxAllowed) {
        int cut = 1;
        int cutSum = 0;
        for (int i = 0; i < nums.length; ++i) {
            if (cutSum + nums[i] <= maxAllowed) {
                cutSum += nums[i];
            } else {
                ++cut;
                cutSum = nums[i];
            }
        }
        return cut;
    }
}