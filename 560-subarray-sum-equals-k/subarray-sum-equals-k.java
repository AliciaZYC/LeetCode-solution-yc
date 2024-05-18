class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer,Integer> map=new HashMap<>();
        map.put(0,1);
        int sum=0,cnt=0;
        for(int x:nums){
            sum+=x;
            if(map.containsKey(sum-k)) cnt+=map.get(sum-k);
            map.put(sum,map.getOrDefault(sum,0)+1);
        }
        return cnt;
    }
}