class Solution {
    public int shipWithinDays(int[] weights, int days) {
        int left=-1,right=-1,sum=0;
        for(int w:weights){
            sum+=w;
            left=Math.max(left,w);
        }
        right=left*(weights.length/days+Integer.signum(weights.length%days));
        left=Math.max(left,sum/days);
        while (left<right){
            int mid=left+(right-left)/2;
            if(good(mid,weights,days)) right=mid;
            else left=mid+1;
        }
        return left;
    }
    public boolean good(int res, int[] weights, int days){
        int sum=0;
        for (int w:weights){
            if(sum+w>res){
                sum=0;
                days--;
            }
            sum+=w;
        }
        return days>0;
    }
}