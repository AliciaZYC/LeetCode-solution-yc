class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def rowbs(l,r,row):
            if not row[l]<=target<=row[r]:
                return
            if l==r:
                return row[l]==target
            mid = l+(r-l)//2
            if row[mid]==target:
                return True
            elif row[mid]<target:
                return rowbs(mid+1,r,row)
            else:
                return rowbs(l,mid,row)
        for row in matrix:
            if rowbs(0,len(row)-1,row):
                return True
        return False