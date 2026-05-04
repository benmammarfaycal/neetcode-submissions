class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left=0
        right=len(heights)-1
        area_max=0
        while left<right:
            largeur=right-left
            hauteur=min(heights[left],heights[right])
            area=largeur*hauteur
            area_max=max(area_max,area)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return area_max
