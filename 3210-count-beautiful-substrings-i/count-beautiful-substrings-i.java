class Solution {
    public int beautifulSubstrings(String s, int k) {
        HashMap<Integer , List<Integer>> map = new HashMap<>();
        map.put(0 , new ArrayList());
        map.get(0).add(-1); //empty substring

        int con=0;
        int vow=0;
        int res=0;
        for(int i=0;i<s.length();i++){
            char ch = s.charAt(i);
            if(ch=='a' || ch=='e' || ch=='i'||ch=='o'| ch=='u'){
                vow++;
            }
            else con++;

            if(map.containsKey(con-vow)){
                List<Integer> temp = map.get(con-vow);
                for(int id:temp){
                    int number = (i-id+1)/2;
                    if((number*number)%k==0) res++;
                }
             map.get(con-vow).add(i);
            }
        
           else{ 
              map.put(con-vow , new ArrayList<>());
              map.get(con-vow).add(i);
           }
        }
        return res;
    }
}