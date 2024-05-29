class Solution {
    public int minimumArrayLength(int[] nums) {
        int min = Integer.MAX_VALUE;
        for(int i : nums){
            min = Math.min(min,i);
        }
        int cnt_min = 0;
        for(int i : nums){
            if(i%min>0)return 1;
            if(min == i){
                cnt_min++;
            }
        }
        if(cnt_min==1)return 1;
        return (cnt_min+1)/2; 
    }
}