class Solution {
    public int maxArea(int[] height) {
        int water=0, left=0, right= height.length-1;
        while(left<right){
            int h = Math.min(height[left], height[right]);
            int w = right - left;
            water=Math.max(water,h*w);
            if (height[left]<height[right]) left++;
            else right--;
        }
        return water;
    }
}