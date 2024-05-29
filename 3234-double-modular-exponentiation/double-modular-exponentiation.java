class Solution {
    public int power(int a, int b,int mod){
        int res = 1;
        for(int i=1; i<=b; i++){
            res *= a;
            res%=mod;
        }
        return res;
    }
    public List<Integer> getGoodIndices(int[][] variables, int target) {
        List<Integer> res = new ArrayList<>();
        for(int i=0; i<variables.length; i++){
            int arr[] = variables[i];
            int pow = power(arr[0],arr[1],10);
            pow = power(pow, arr[2], arr[3]);
            if(pow == target) res.add(i);
        }
        return res;
    }
}