class Solution {
    public int beautifulSubstrings(String s, int k) {
        int count = 0, n = s.length();
        for (int i = 0; i < n; i++) {
            int vowels = 0, conso = 0;
            for (int j = i; j < n; j++) {
                if (isVowel(s.charAt(j))) vowels++;
                else conso++;
                if (vowels == conso && (vowels * conso) % k == 0) count++;
            }
        }
        return count;
    }

    public boolean isVowel(char c) {
        return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
    }
}
