class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo=[-1]*len(nums)
        def dfs(i):
            if i>=len(nums):
                return 0
            if memo[i]!=-1:
                return memo[i]
            res=1
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    res=max(res,1+dfs(j))
            memo[i]=res
            return res
        return max(dfs(i) for i in range(len(nums)))