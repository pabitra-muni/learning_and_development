# https://leetcode.com/problems/trapping-rain-water/?envType=problem-list-v2&envId=array


"""
Optimal Dynamic Programming Solution:
Precompute Left Max Array (left_max[]):

    left_max[i] stores the maximum height from index 0 to i.

Precompute Right Max Array (right_max[]):

    right_max[i] stores the maximum height from index i to n-1.

Compute Water Trapped at Each Index:

    Water at i = min(left_max[i], right_max[i]) - height[i], if positive.

"""
class RainWaterTrap:
    def trap(self, height: list[int]) -> int:
        if not height or len(height) < 3:
            return 0  # At least 3 bars are needed to trap water

        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        trapped_water = 0

        # Compute left max for each index
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        # Compute right max for each index
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        # Compute trapped water
        for i in range(n):
            trapped_water += max(0, min(left_max[i], right_max[i]) - height[i])

        return trapped_water
