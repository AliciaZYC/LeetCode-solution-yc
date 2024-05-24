class Solution {
    Boolean[] memo;
    public boolean wordBreak(String s, List<String> wordDict) {
        int n=s.length();
        memo= new Boolean[n+1];
        return dfs(s,n,new HashSet<>(wordDict));
    }
    private boolean dfs(String s, int len, Set<String> dict){
        if(len==0){
            return true;
        }
        if(memo[len]!=null){
            return memo[len];
        }
        memo[len]=false;
        for(int i=0;i<len;i++){
            boolean right=dict.contains(s.substring(i,len));
            if(!right) continue;
            boolean left=dfs(s,i,dict);
            if(left){
                memo[len]=true;
                break;
            }
        }
        return memo[len];
    }
}