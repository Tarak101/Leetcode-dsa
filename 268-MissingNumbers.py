class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        xor_total=0
        xor=0
        for i in range(n+1):
            xor_total ^= i
        for num in nums:
            xor ^= num
        return xor_total^xor