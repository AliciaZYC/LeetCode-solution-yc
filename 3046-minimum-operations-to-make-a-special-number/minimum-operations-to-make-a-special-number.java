class Solution {
    public int minimumOperations(String num) {
        int l=num.length();
        int ans=l;
        int ind=num.lastIndexOf("5"),ind1=num.lastIndexOf("0");
        if(ind1!=-1){
            for(int i=ind1-1;i>=0;i--){
                char c=num.charAt(i);
                if(c=='0'||c=='5'){
                    int val=l-(ind1+1);
                    val=val+(ind1-(i+1));
                    ans=Math.min(ans,val);
                }
            }
            ans=Math.min(ans,l-1);
        }
        if(ind!=-1){
            for(int i=ind-1;i>=0;i--){
                char c=num.charAt(i);
                if(c=='2'||c=='7'){
                    int val=l-(ind+1);
                    val=val+(ind-(i+1));
                    ans=Math.min(ans,val);
                }
            }
            ans=Math.min(ans,l);
        }
        return Math.min(ans,l);
    }
}