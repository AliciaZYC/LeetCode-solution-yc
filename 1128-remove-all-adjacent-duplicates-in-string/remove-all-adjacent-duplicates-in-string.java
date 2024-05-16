class Solution {
    public String removeDuplicates(String s) {
        char[] a = s.toCharArray();
        int right=-1;
        for (char c:a){
            if (right>=0 && a[right]==c) --right;
            else a[++right]=c;
        }
        return String.valueOf(a,0,right+1);
    }
}