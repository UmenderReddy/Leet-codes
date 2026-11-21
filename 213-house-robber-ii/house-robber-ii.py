class Solution:
    def rob(self, nums: list[int]) -> int:
        
        def rob1(nums):
            if len(nums)==1:
                return nums[0]
            dp=[-1]*len(nums)
            dp[0]=nums[0]
            dp[1]=max(nums[0],nums[1])
            for i in range(2,len(nums)):
                dp[i]=max(dp[i-1],nums[i]+dp[i-2])
            return dp[-1]

        if len(nums)==1:
            return nums[0]
        return max(rob1(nums[1:]),rob1(nums[:-1]))