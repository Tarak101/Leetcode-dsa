class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low,high=0,len(nums)-1
        mid=(low+high)//2
        for i in nums:
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low=mid+1
                mid=(low+high)//2
            else:
                high=mid-1
                mid=(low+high)//2
        return mid+1