class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = 0
        count =0
        for i in range(len(nums)):
            if count == 0:
                target = nums[i]
                count =1
            # count ！= 0
            elif target != nums[i]:
                count -=1
            else:
                count +=1
        return target
        # 上面这个的逻辑是：majarity的一定是出现数量大于1/2的，就是它可以被任何一个其他的抵消，但是仍有多
        # counts = collections.Counter(nums)
        # return max(counts.keys(),key=counts.get)
      