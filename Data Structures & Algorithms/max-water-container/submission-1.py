class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        maxi=0
        while left<len(heights):
            right=left+1
            while right<len(heights):
                i=right-left
                h=min(heights[left],heights[right])
                s=i*h
                maxi=max(maxi,s)

                right+=1
            left+=1
        return maxi
