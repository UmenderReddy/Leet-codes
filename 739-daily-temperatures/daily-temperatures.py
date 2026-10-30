class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        s=[]
        n=len(temperatures)
        ans=[0]*n
        for i in range(n):
            while s and temperatures[i]>temperatures[s[-1]]:
                prev=s.pop()
                ans[prev]=i-prev
            s.append(i)
        return ans