class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        else:
            rows=[[]for row in range(numRows)]
            index=0
            # step=1
            for char in s:
                rows[index].append(char)
                if index==0:
                    step=1#downwards
                if index==numRows-1:
                    step=-1#upwards
                index+=step
            for i in range(numRows):
                rows[i]=''.join(rows[i])
            return ''.join(rows)
           
            