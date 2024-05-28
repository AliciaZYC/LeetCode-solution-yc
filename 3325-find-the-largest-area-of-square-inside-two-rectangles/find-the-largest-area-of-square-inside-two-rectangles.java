class Solution {
    public long largestSquareArea(int[][] bottomLeft, int[][] topRight) {
        int n = bottomLeft.length, ans = 0;
        for(int i=0; i<n; i++){
            for(int j=i+1; j<n; j++){
                int[] startpoint = new int[2];
                startpoint[0] = Math.max(bottomLeft[i][0], bottomLeft[j][0]);
                startpoint[1] = Math.max(bottomLeft[i][1], bottomLeft[j][1]);
                int[] endpoint = new int[2];
                endpoint[0] = Math.min(topRight[i][0], topRight[j][0]);
                endpoint[1] = Math.min(topRight[i][1], topRight[j][1]);
                if(endpoint[0] > startpoint[0] && endpoint[1] > startpoint[1]) {
                    int diff1 = endpoint[0]-startpoint[0];
                    int diff2 = endpoint[1]-startpoint[1];
                    int min = Math.min(diff1 , diff2);
                    ans = Math.max(min, ans);
                }
            }
        }
        return ans*1l*ans;
    }
}