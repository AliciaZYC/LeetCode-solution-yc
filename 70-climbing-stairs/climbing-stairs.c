int climbStairs(int n) {
    if (n==1) return 1;
    int pre_1=1, pre_2=1,cur;
    for (int i=1;i<n;i++){
        cur=pre_1+pre_2;
        pre_2=pre_1;
        pre_1=cur;
    }
    return cur;
}