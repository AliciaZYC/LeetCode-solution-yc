class Solution:
    def intToRoman(self, num: int) -> str:
        num = [int(digit) for digit in str(num)][::-1] # Convert num to little endian
        roman = ""
        for i in range(len(num)): # iterate through the array of integers
            if i == 0: # 1-9
                if num[0] == 4:
                    roman = "IV"
                elif num[0] == 9:
                    roman = "IX"
                else:
                    # if num[i] >= 5: roman = "V" + (num[i]-5)*"I"
                    # else: roman = "I"*num[i]
                    roman = "V" + (num[i]-5)*"I" if num[i] >= 5 else "I"*num[i]
            elif i == 1: # 10-99
                if num[i] == 4:
                    roman = "XL" + roman
                elif num[i] == 9:
                    roman = "XC" + roman
                else:
                    roman = "L" + "X"*(num[i]-5) + roman if num[i] >= 5 else "X"*num[i] + roman
            elif i == 2: # 100-999
                if num[i] == 4:
                    roman = "CD" + roman
                elif num[i] == 9:
                    roman = "CM" + roman
                else:
                    roman = "D" + "C"*(num[i]-5) + roman if num[i] >= 5 else "C"*num[i] + roman
            elif i == 3: # 1000+
                roman = num[i]*"M" + roman
        return roman