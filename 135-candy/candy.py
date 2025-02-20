class Solution:
    def candy(self, ratings: List[int]) -> int:
        result=[1]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                result[i]=result[i-1]+1
        for j in range(len(ratings)-2,-1,-1):
            if ratings[j]>ratings[j+1] and result[j]<result[j+1]+1:
                result[j]=result[j+1]+1
        return sum(result)