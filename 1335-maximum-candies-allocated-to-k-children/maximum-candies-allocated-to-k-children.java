class Solution {
    public int maximumCandies(int[] candies, long k) {
        long sum = 0;
        for(int i = 0 ; i < candies.length; i++){
            sum+= candies[i];
        }
        int left = 1;
        int right = (int)(sum/k);
        
        while(left <= right){
            int mid = (right - left) / 2 + left;
            long count = 0;
            
            for(int i = 0 ; i < candies.length; i++){
                count+= candies[i]/mid;
            }
            if(count >= k){
                left = mid+1;
            }
            else{
                right = mid-1;
            }
        }
        return right;
    }
}