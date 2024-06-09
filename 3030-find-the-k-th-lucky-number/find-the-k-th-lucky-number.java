class Solution {
    public String kthLuckyNumber(int k) {
        int n=1;
        for(;k>(1<<n);k-=1<<n++);
        char[] t = new char[n];
        for (--k; --n >= 0; t[n] = (k & 1) > 0 ? '7' : '4', k >>= 1);
        return String.valueOf(t);
    }
}