class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        results = []
        
        def backtrack(start_index, current_path):
            # 1. Base Case / Solution Capture
            # In subsets, every path we take is a valid mathematical subset
            results.append(list(current_path))
            
            # 2. Iterate through choices (the remaining numbers)
            for i in range(start_index, len(nums)):
                # 3. Make a choice
                current_path.append(nums[i])
                
                # 4. Explore (move to the next number)
                backtrack(i + 1, current_path)
                
                # 5. Backtrack (undo the choice)
                current_path.pop()
        
        backtrack(0, [])
        return results