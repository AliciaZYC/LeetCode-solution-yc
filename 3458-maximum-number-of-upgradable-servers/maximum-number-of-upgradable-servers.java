class Solution {
    public int[] maxUpgrades(int[] count, int[] upgrade, int[] sell, int[] money) {
        int n=count.length;
        int[] ans=new int[n];
        for(int i=0;i<n;++i){
            ans[i]=getMax(count[i],upgrade[i],sell[i],money[i]);
        }
        return ans;
    }
    private int getMax(long servers,long eachUpgradeCost,long eachSellCost, long money){
        long low=0,high=servers,ans=0;
        while(low<=high){
            long mid=low+(high-low)/2;
            long totalCost=mid*eachUpgradeCost;
            long totalMoney=money+(servers-mid)*eachSellCost;
            if (totalMoney>=totalCost){
                ans=mid;
                low=mid+1;
            }else{
                high=mid-1;
            }
        }
        return (int) ans;
    }
}