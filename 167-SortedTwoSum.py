class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,n in enumerate(nums): #Using enumerate function so that i can get both value and index
            diff = target - n
            if diff in seen: #checking if diff value exists in seen
                return [seen[diff],i] 
            seen[n]=i #put the value if it doesnt exist