class Solution {
    public int maximumPrimeDifference(int[] nums) {
        int minIndex=-1,maxIndex=-1;
        for(int i=0;i<nums.length;i++){
            if(isPrime(nums[i])){
                if(minIndex==-1){
                    minIndex=i;
                }
                maxIndex=i;
            }
        }
        if(minIndex!=-1)return maxIndex-minIndex;
        return 0;
    }
    boolean isPrime(int number){
        if (number<=1) return false;
        for(int i=2;i*i<=number;i++){
            if(number%i==0){
                return false;
            }
        }
        return true;
    }
}