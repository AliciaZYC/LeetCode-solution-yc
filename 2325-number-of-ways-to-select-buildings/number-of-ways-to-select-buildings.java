class Solution {
    public long numberOfWays(String s) {
        int zeroCount=0,oneCount=0;
        long zeroOneCount=0,oneZeroCount=0;
        long answer=0;
        for(char c:s.toCharArray()){
            if(c=='0'){
                answer+=zeroOneCount;
                oneZeroCount += oneCount;
                zeroCount++;
            }else{
                answer += oneZeroCount;
                zeroOneCount += zeroCount;
                oneCount++;
            }
        }
        return answer;
    }
}