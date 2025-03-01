"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element 
appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were 
present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

"""
class Duplicate:
    def rearrangeDuplicates(self, numbers: list[int]) -> int:
        currentVal = numbers[0]
        uniquePositon = 0
        for i in range(1, len(numbers)):
            if currentVal != numbers[i]:
                currentVal = numbers[i]
                numbers[i] = numbers[uniquePositon + 1]
                numbers[uniquePositon + 1] = currentVal
                uniquePositon += 1
        return uniquePositon + 1
