class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res=new ArrayList<>();
        dfs(res,nums,0);
        return res;
    }
    private void dfs(List<List<Integer>> res,int[] nums,int index){
        if(index>=nums.length){
            List<Integer> ans=new ArrayList<>();
            for(int i=0;i<nums.length;i++){
                ans.add(nums[i]);
            }
            res.add(ans);
            return;
        }
        for (int i=index;i<nums.length;i++){
            swap(nums,index,i);
            dfs(res,nums,index+1);
            swap(nums,index,i);
        }
    }
    private void swap(int[]nums, int i1,int i2){
        int tmp=nums[i1];
        nums[i1]=nums[i2];
        nums[i2]=tmp;
    }

}