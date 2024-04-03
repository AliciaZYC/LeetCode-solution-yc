class Solution {
    public int minMeetingRooms(int[][] intervals) {
        int n=intervals.length;
        int[] starts=new int[n];
        int[] ends=new int[n];
        for( int i=0; i<n; i++){
            starts[i]=intervals[i][0];
            ends[i]=intervals[i][1];
        }
        Arrays.sort(starts);
        Arrays.sort(ends);
        int rooms=0, endsItr=0;
        for(int i=0; i<n; i++){
            if(starts[i]<ends[endsItr]) rooms++;
            else endsItr++;
        }
        return rooms;
    }
}