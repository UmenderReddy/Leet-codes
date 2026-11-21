class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=0
        r=0
        h=len(nums)-1
        while r<=h:
            if nums[r]==0:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r+=1
            elif nums[r]==1:
                r+=1
            else:
                nums[h],nums[r]=nums[r],nums[h]
                h-=1