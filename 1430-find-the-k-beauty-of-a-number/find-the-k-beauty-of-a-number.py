class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        x=str(num)
        c=0
        for i in range(len(x)-k+1):
            a=int(x[i:i+k])
            if a!=0 and num%a==0:
                c+=1
        return c

