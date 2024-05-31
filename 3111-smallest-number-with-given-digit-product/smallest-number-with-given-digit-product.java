class Solution {
    public String smallestNumber(long n) {
        if(n<10)return String.valueOf(n);
        StringBuilder stringBuilder=new StringBuilder();
        for(int i=9;i>1&&n>1;i--){
            while(n%i==0){
                stringBuilder.append(i);
                n=n/i;
            }
        }
        if(n!=1) return "-1";
        return stringBuilder.reverse().toString();
    }
}