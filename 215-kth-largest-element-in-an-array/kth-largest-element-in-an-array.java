class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> heap=new PriorityQueue<>();
        for (int x:nums){
            if(heap.size()<k||x>=heap.peek()) heap.offer(x);
            if(heap.size()>k) heap.poll();
        }
        return heap.peek();
    }
}