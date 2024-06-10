class Solution {
    public int numberOfRounds(String loginTime, String logoutTime) {
        int start = timeInMinute(loginTime); 
        int end = timeInMinute(logoutTime);
        
        if(end < start)
            end += 24*60;
        if(start % 15 != 0)
            start += 15 - (start % 15); 
        if(end % 15 != 0)
            end -= end % 15; 
        if(end < start)
            return 0;
        
        return (end-start)/15;
        
    }
    
    private int timeInMinute(String s){
        int h = Integer.parseInt(s.substring(0,2));
        int m = Integer.parseInt(s.substring(3));
        
        return (h*60)+m;
    }
}