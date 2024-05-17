class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n=temperatures.length;
        int[] res= new int [n];
        Deque<Integer> stack=new ArrayDeque<>();
        for (int i=n-1;i>=0;i--){
            while(!stack.isEmpty()&&temperatures[i]>=temperatures[stack.peek()]) stack.pop();
            if(stack.isEmpty()) res[i]=0;
            else res[i]=stack.peek()-i;
            stack.push(i);
        }
        return res;
    }
}