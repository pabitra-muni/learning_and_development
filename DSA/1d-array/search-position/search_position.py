# https://leetcode.com/problems/search-insert-position/description/?envType=problem-list-v2&envId=array

class SearchPosition:
    # below has O(n) complexity
    def searchInsertPosition(self, numbers: list[int], target: int) -> int:
        length = len(numbers)

        for i in range(length):
            if numbers[i] == target or numbers[i] > target:
                return i
        return length
    
    # below has O(log n) complexity
    def searchInsertPositionImproved(self, numbers: list[int], target: int) -> int:
        length = len(numbers)
        index = length//2
        if numbers[index] == target:
            return index
        if numbers[index] < target:
            index += 1
            while index < length and numbers[index] < target:
                index += 1
            return index
        else:
            index -= 1
            while index >= 0 and numbers[index] >= target:
                if index == 0: return 0
                index -= 1
            return index + 1

