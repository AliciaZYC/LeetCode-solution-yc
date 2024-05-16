class Solution {
    public int longestRepeatingSubstring(String s) {
        int l=0,r=s.length()-1;
        while(l<r){
            int mid=l+(r-l+1)/2;
            if (f(s,mid)) l=mid;
            else r=mid-1;
        }
        return l;
    }
    public boolean f(String s, int length){
        Set<String> seen=new HashSet<>();
        for(int i=0;i<=s.length()-length;i++){
            int j=i+length-1;
            String sub=s.substring(i,j+1);
            if (seen.contains(sub)) return true;
            seen.add(sub);
        }
        return false;
    }
}