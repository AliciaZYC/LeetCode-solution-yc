class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res= new ArrayList<>();
        dfs(res,nums,new ArrayList<>(),0);
        return res;
    }
    public void dfs(List<List<Integer>> res,int[] nums, List<Integer> cur, int index){
        if(index>=nums.length){
            res.add(new ArrayList<>(cur));
            return;
        }
        cur.add(nums[index]);
        dfs(res,nums,cur,index+1);
        cur.remove(cur.size()-1);
        dfs(res,nums,cur,index+1);
    }
}