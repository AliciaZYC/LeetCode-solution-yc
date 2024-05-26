class Solution {
    static boolean isNotPrime[] = new boolean[101];
    static {
        isNotPrime[1] = true;
        for (int i = 2; i <= Math.sqrt(isNotPrime.length - 1); i++) {
            if (!isNotPrime[i]) {
                for (int j = i * i; j < isNotPrime.length; j += i) {
                    isNotPrime[j] = true;
                }
            }
        }
    }

    public int maximumPrimeDifference(int[] nums) {
        int left = 0, right = nums.length - 1;
        while (isNotPrime[nums[left]]) {
            left++;
        }
        while (isNotPrime[nums[right]]) {
            right--;
        }
        return right - left;
    }
}