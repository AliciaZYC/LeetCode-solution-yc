class Solution {
    public List<List<Integer>> findWinners(int[][] matches) {
        int[] arr = new int[100000];
        for (int[] match : matches) {
            if (arr[match[0] - 1] == 0) {
                arr[match[0] - 1]++;
            }
            if (arr[match[1] - 1] > 0) {
                arr[match[1] - 1] = -1;
            }else {
                arr[match[1] - 1]--;
            }
        }
        List<Integer> wins = new ArrayList<>();
        List<Integer> lose = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 1) {
                wins.add(i + 1);
            }
            if (arr[i] == -1) {
                lose.add(i + 1);
            }
        }
       

        List<List<Integer>> list = new ArrayList<>();
        list.add(wins);
        list.add(lose);

        return list;
    }
}