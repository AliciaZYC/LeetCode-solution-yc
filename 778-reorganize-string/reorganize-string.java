class Solution {
    public String reorganizeString(String s) {
        int[][] map=new int[26][2];
        for(int i=0 ; i<26 ; ++i) {
            map[i][0]=i;
        }
        char[] ch=s.toCharArray();
        for(char c: ch) {
            map[c-'a'][1]++;
        }
        Arrays.sort(map, (a,b)->b[1]-a[1]);
        int ind=0, n=s.length(), mod=(n%2)==0? n-1: n;
        if(map[0][1]>(n+1)/2) return "";
        for(int i=0;i<26;++i) {
            while(map[i][1]-->0) {
                int pos = ind==mod? mod: (ind*2)%mod;
                ch[pos]=(char)(map[i][0]+'a');
                ind++;
            }
        }
        return new String(ch);
    }
}