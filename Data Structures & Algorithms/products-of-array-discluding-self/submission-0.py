class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        pref = 1
        post = 1
        for i in range(len(res)):
            res[i] = pref
            pref *= nums[i]
        for j in range(len(res) - 1, -1, -1):
            res[j] *= post
            post *= nums[j]
        return res

        