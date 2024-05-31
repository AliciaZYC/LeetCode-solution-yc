class Solution {
    public int maximumXorProduct(long a, long b, int n) {
        long tmpa=a,tmpb=b;
        long mask=((1L<<n)-1);
        tmpa=(tmpa&~mask);
        tmpb=(tmpb&~mask);
        for (int i=n-1;i>=0;--i){
            if(((a>>i)&1)==((b>>i)&1)){
                tmpa=((tmpa)|(1L<<i));
                tmpb=((tmpb)|(1L<<i));
            }else{
                if(tmpa>tmpb){
                    tmpb=((tmpb)|(1L<<i));
                }else{
                    tmpa=((tmpa)| (1L<<i));
                }
            }
        }
        int MOD = 1_000_000_007;
        long finalans = ((tmpa%MOD) * (tmpb%MOD)) %MOD;
        return (int)finalans;
    }
}