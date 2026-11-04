class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        z=path.split("/")
        for x in z:
            if x=="" or x== ".":
                continue
            elif x=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(x)
        return "/"+"/".join(stack)