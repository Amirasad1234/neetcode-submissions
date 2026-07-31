class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for i in range(len(nums)):
            dp2 = defaultdict(int)
            for cur_sum, count in dp.items():
                dp2[cur_sum + nums[i]] += count
                dp2[cur_sum - nums[i]] += count
            dp = dp2
        return dp[target]












        