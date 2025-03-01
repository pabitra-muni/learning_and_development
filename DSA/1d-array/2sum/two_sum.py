# using sorted array...
# sorting - O(logn)
# storing sorted array - O(n) : space
# iteration - O(n)
# total - O(nlogn): time, O(n): space

class TwoSum:
    def twoSumWithSortedArray(self, nums: list[int], target: int) -> list[int]:
        temp = nums.copy()
        nums.sort()
        left = 0
        right = len(nums) - 1
        twoSumPositions = []
        while left < right:
            currentSum = nums[left] + nums[right]
            if  currentSum == target:
                for i in range(len(temp)):
                    if temp[i] == nums[left] or temp[i] == nums[right]:
                        twoSumPositions.append(i)
                return twoSumPositions
            if currentSum < target:
                left += 1
            else:
                right -= 1
        return twoSumPositions        

    #################################
    #################################
    # using hash map
    # total O(n): time, O(n): space - for the map
    def twoSumWithMap(self, nums: list[int], target: int) -> list[int]:
        num_map = {}  # Dictionary to store numbers and their indices
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in num_map:
                return [num_map[remaining], i]
            num_map[num] = i
        return [] 