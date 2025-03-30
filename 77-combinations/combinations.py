class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol=[]
        def backtrack(remain,combination,nex):
			# solution found
            if remain==0:
                sol.append(combination.copy())
            else:
				# iterate through all possible candidates
                # nex：防止重复「2，3」--「3，2」
                for i in range(nex,n+1):
					# add candidate
                    combination.append(i)
					#backtrack
                    backtrack(remain-1,combination,i+1)
					# remove candidate
                    combination.pop()
            
        backtrack(k,[],1)
        return sol
'''
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)
'''