class Solution {
    public int numberOfPairs(int[][] points) {
        int n = points.length,ans = 0;
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                int x1 = points[i][0],y1 = points[i][1],x2 = points[j][0],y2 = points[j][1];
                if(!checkPosition(x1,y1,x2,y2)){
                    continue;
                }
                boolean flag = true;
                for(int k=0;k<n;k++){
                    if(k==i || k==j) continue;
                    if(!flag) break;
                    int x = points[k][0],y = points[k][1];
                    if(x>=Math.min(x1,x2) && x<=Math.max(x1,x2) && y>=Math.min(y1,y2) && y<=Math.max(y1,y2) ) flag = false;
                }
                if(flag) ans++;
            }
        }
        return ans;
    }
    public boolean checkPosition(int x1,int y1,int x2,int y2){
        if((x1>=x2 && y2>=y1) || (x1<=x2 && y1>=y2)) return true;
        return false;
    }
}