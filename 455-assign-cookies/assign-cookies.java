class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        int child=0,cookie=0;
        while(child<g.length && cookie<s.length){
            if(g[child]<=s[cookie]){
                child+=1;
            }
            cookie+=1;
        }
        return child;
    }
}