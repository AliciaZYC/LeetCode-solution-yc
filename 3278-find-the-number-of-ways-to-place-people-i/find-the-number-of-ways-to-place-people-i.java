class Solution {
    public int numberOfPairs(int[][] points) {
        int n = points.length;
        Arrays.sort(points, (a, b) -> a[0] == b[0] ? b[1] - a[1] : a[0] - b[0]);
        int cnt = 0;
        for (int i = 0; i < n - 1; i++) {
            int highest=-1;
            for (int j = i + 1; j < n; j++) {
                if (j == i + 1) {
                    if (points[j][1] <= points[i][1]) {
                        cnt++;
                        highest=points[j][1];
                    }
                } else {
                    if (points[j][1] <= points[i][1] && points[j][1]>highest) {
                        cnt++;
                        highest=points[j][1];
                    }
                }
            }
        }
        return cnt;
    }
}