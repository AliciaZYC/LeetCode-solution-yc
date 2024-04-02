class Solution {
    public List<Integer> partitionLabels(String s) {
        int []lastIndex=new int [26];
        List<Integer> ans= new ArrayList<>();
        for (int i=0; i<s.length(); i++){
            lastIndex[s.charAt(i)-'a']=i;
        }
        int end = 0, prev =0;
        for (int j=0;j<s.length();j++){
            end = Math.max(end, lastIndex[s.charAt(j) - 'a']);
            if (end==j){
                ans.add(end+1-prev);
                prev=j+1;
            }
        }
        return ans;
    }
}