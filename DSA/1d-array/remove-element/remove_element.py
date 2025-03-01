# https://leetcode.com/problems/remove-element/description/?envType=problem-list-v2&envId=array
class RemoveElement:
    def removeDuplicateElement(self, numbers: list[int], value: int) -> int:
        left = 0
        right = len(numbers) -1

        while left <= right:
            if numbers[left] == value:
                if left < right:
                    temp = numbers[right]
                    numbers[right] = numbers[left]
                    numbers[left] = temp
                right -= 1
            else:
                left += 1
        return left
