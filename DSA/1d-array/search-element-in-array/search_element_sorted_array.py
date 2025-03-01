#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/?envType=problem-list-v2&envId=array

class ElementSearch:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lastIndex = len(nums) - 1
        positions = [-1, -1]
        if lastIndex > 0:
            index = self.__helper(nums, target, 0, lastIndex)
            if index != -1:
                left = index
                right = index
                while left >= 0 or right <= lastIndex:
                    if left >= 0 and nums[left] == target: 
                        positions[0] = left
                    if right <= lastIndex and nums[right] == target:
                        positions[1] = right 
                    left -= 1
                    right += 1
                    
        #handle single element and empty array
        elif lastIndex == 0 and target == nums[0]:
            positions[0] = 0
            positions[1] = 0
        
        return positions

    def __helper(self, nums: list[int], target: int, left: int, right: int) -> int:
        mid = (right + left) // 2
        index = -1
        while index == -1 and left <= right:
            if target == nums[mid]:
                 index = mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
            mid = (right + left) // 2
        return index