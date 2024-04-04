class Solution {
    public int minOperations(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int cnt=0;
        for( int num:nums){
            map.put(num, map.getOrDefault(num, 0)+1);
        }
        for (int count:map.values()){
            if(count==1)return -1;
            cnt+=count/3;
            if(count%3!=0)cnt++;
        }
        return cnt;
    }
}