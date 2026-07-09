class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, num in enumerate(nums):
            dif = target - num
            if dif in indices:
                return [indices[dif], i]
            indices[num] = i
        return []
        
