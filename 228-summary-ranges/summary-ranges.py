class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        else:
            start=nums[0]
            result=[]
            for i in range(1,len(nums)):
                if nums[i]!=nums[i-1]+1:
                    end=nums[i-1]
                    if start==end:
                        str_range=str(start)
                        result.append(str_range)
                    else:
                        str_range=str(start)+"->"+str(end)
                        result.append(str_range)
                    start=nums[i]
            end = nums[-1]
            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}->{end}")
        return result


