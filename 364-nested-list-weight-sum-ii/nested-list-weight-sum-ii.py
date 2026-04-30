# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        unweighted, weighted = 0, 0
        
        while nestedList:
            next_level = []
            for nested in nestedList:
                if nested.isInteger():
                    unweighted += nested.getInteger()
                else:
                    next_level.extend(nested.getList())
            weighted += unweighted          # accumulate each level's running sum
            nestedList = next_level
        
        return weighted

"""
unweighted: 累加当前层及之前所有层的整数总和
weighted: 最终结果，每层都会加上当前的 unweighted
假设嵌套列表是 [[1,1],2,[1,1]]：
第1层：遇到 2，unweighted = 2，weighted = 2
第2层：遇到 1,1,1,1，unweighted = 2+4 = 6，weighted = 2+6 = 8
最终结果 8 = 2×2 + 1×1 + 1×1 + 1×1 + 1×1，正好符合深度越深权重越小的要求！
"""