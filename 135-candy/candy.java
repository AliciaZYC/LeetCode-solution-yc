class Solution {
    public int candy(int[] ratings) {
        int l = ratings.length;
        int[] res = new int[l];
        Arrays.fill(res, 1);
        for (int i=1;i<l;i++){
            if (ratings[i]>ratings[i-1]){
                res[i]=res[i-1]+1;
            }
        }
        for (int j=l-2;j>=0;j--){
            if (ratings[j]>ratings[j+1]&&res[j]<=res[j+1]){
                res[j]=res[j+1]+1;
            }
        }
        int sum=0;
        for (int k = 0; k < res.length; k++) {
            sum += res[k];
        }
        return sum;
    }
}