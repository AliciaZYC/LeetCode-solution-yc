class Solution {
    public int maximizeSweetness(int[] sweetness, int k) {
        int person =k+1,totalSweetness=0;
        for (int i: sweetness){
            totalSweetness+=i;
        }
        int left=1,right=totalSweetness/person;
        while(left<=right){
            int mid=left+(right-left)/2;
            if(check(sweetness,mid,person)){
                left=mid+1;
            }else{
                right=mid-1;
            }
        }
        return right;
    }
    public boolean check(int[] sweetness,int goal,int persons){
        int pieces=0,sum=0;
        for (int i:sweetness){
            sum+=i;
            if(sum>=goal){
                pieces++;
                sum=0;
            }
        }
        return pieces>=persons;
    }
}