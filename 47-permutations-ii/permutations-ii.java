class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> res=new ArrayList<>();
        permutation(res,nums,0);
        return res;
    }
    private void permutation(List<List<Integer>> res,int[] nums,int index){
        if(index==nums.length){
            List<Integer> ans=new ArrayList<>();
            for(int x:nums){
                ans.add(x);
            }
            res.add(ans);
            return;
        }
        Set<Integer> visited= new HashSet<>();
        for (int i=index;i<nums.length;i++){
            swap(nums,index,i);
            if (visited.add(nums[index])){
                permutation(res,nums,index+1);
            }
            swap(nums,index,i);
        }
    }
    private void swap(int[]nums, int i1,int i2){
        int tmp=nums[i1];
        nums[i1]=nums[i2];
        nums[i2]=tmp;
    }
}