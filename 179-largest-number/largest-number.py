class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # res=[]
        # for e in nums:
        #     res += [str(e)]
        # n=len(res)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if str(res[i])+str(res[j])>str(res[j])+str(res[i]):
        #             continue
        #         else:
        #             res[i],res[j]=res[j],res[i]
        # ans=''.join(res)
        # if int(ans)==0:
        #     return "0"
        # return ans
        arr = list(map(str,nums))
        arr.sort(key=lambda x:x*10, reverse=True)
        if arr[0]=="0":
            return "0"
        largest=''.join(arr)
        return largest