# https://leetcode.com/problems/search-in-rotated-sorted-array/?envType=problem-list-v2&envId=array

class RotatedArraySearch:
    def search(self, nums: list[int], target: int) -> int:
        length = len(nums)
        rLeft = length - 1
        rRight =  length - 1
        left = 0
        right = length -1
        # the array is rotated if last element is smaller than first element
        if(nums[-1] < nums[0]):
            # keep moving from right to left to find the smallest element
            rRightValue = nums[rRight]
            rLeftValue = nums[rRight]
            while rLeftValue <= rRightValue:
                rLeft -= 1
                rLeftValue = nums[rLeft]
            right = rLeft
            rLeft += 1
            
            if target <= nums[rRight]:
                left = rLeft
                right = rRight
        return self.__helper(nums, target, left, right)


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


