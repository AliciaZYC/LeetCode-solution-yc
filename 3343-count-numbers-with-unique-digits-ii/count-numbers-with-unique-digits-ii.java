class Solution {
    public int numberCount(int a, int b) {
        int count = 0;


        for(int i = a; i <= b; i++) {
            int ones = i % 10;
            int tens = (i/10) % 10;


            int hundreds = i/100;

            if(ones == tens) {
                continue;
            }

            if(tens == hundreds && tens != 0) {
                continue;
            }

            if(hundreds == ones && hundreds != 0) {
                continue;
            }
            count++;
        }
        return count;
    }
}