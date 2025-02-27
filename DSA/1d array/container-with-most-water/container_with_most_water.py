# https://leetcode.com/problems/container-with-most-water/description/?envType=problem-list-v2&envId=array

class WaterContainer:
    def maxArea(self, heights: list[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0
        while left < right:
            curArea = self.__getArea(heights, left, right)
            if curArea > maxArea: maxArea = curArea
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return maxArea

    def __getArea(self, height: list[int], left: int, right: int) -> int:
        return min(height[left], height[right]) * (right - left)