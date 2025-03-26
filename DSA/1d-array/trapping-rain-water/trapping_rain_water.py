# https://leetcode.com/problems/trapping-rain-water/?envType=problem-list-v2&envId=array

class RainWaterTrap:
    def trap(self, heights: list[int]) -> int:
        length = len(heights)
        sumArr = [0] * length
        maxIndex = 0
        lastVal = heights[0]
        total = 0
        for i in range(1, length):
            if heights[i] > lastVal:
                minVal = min(heights[i], heights[maxIndex])
                for j in range(maxIndex, i):
                    posVal =  minVal - heights[j]
                    if posVal > sumArr[j]:
                        total += posVal - sumArr[j]
                        sumArr[j] = posVal
                if heights[i] >= heights[maxIndex]: maxIndex = i

            lastVal = heights[i]
        return total