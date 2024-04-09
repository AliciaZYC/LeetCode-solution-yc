class Solution {
    public int leastInterval(char[] tasks, int n) {
        int []map = new int[26];
        for(char c: tasks){
            map[c-'A']++;
        }
        Arrays.sort(map);
        int batchCnt = map[25];
        int vacantSlots = --batchCnt * n;
        for(int indx = 0; indx <25; indx ++){
            vacantSlots -= Math.min(map[indx],batchCnt);
        }
        return vacantSlots >0?tasks.length+vacantSlots:tasks.length;
    }
}