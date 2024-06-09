class Solution {
    public int numberCount(int a, int b) {
        int[] nums=get(b);
        int n=nums.length;
        int[][][]memo=new int[n+1][1<<10][2];
        assignDefault(memo);
        int max = dfs(nums, 0, 0, true, 0, memo);
        nums = get(a-1); 
        n = nums.length;
        memo = new int[n+1][1<<10][2];
        assignDefault(memo);
        int min = dfs(nums, 0, 0, true, 0, memo);
        return max-min;
    }   
    int[] get(int x) {
        int n = String.valueOf(x).length(), i = n-1;
        int[] nums = new int[n];
        while(x>0){
            nums[i--]=x%10;
            x/=10;
        }
        return nums;
    }
    void assignDefault(int[][][] memo){
        for(int[][] memo1:memo){
            for(int[] memo2:memo1){
                Arrays.fill(memo2,-1);
            }
        }
    }
    int dfs(int[] nums,int i, int mask,boolean limit,int value, int[][][]memo){
        if(i==nums.length) return 1;
        int k=limit?1:0;
        if(memo[i][mask][k]!=-1) return memo[i][mask][k];
        int n=limit?nums[i]:9;
        int sum=0;
        for(int num=0;num<=n;num++){
            if((mask&1<<num)!=0) continue;
            int nextMask=value+num==0?0:mask|1<<num;
            sum+=dfs(nums,i+1,nextMask,limit&&num==n,value+num,memo);
        }
        return memo[i][mask][k]=sum;
    }
}