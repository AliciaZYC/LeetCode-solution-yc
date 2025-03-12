class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for e in path.split('/'):
            if e!="." and e!="" and e!="..":
                stack.append(e)
            elif e==".." and len(stack):
                stack.pop()
        return "/"+"/".join(stack)