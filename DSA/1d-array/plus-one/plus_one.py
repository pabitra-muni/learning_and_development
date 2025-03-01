# https://leetcode.com/problems/plus-one/description/?envType=problem-list-v2&envId=array

class PlusOne:
    def doPlusOne(self, digits: list[int]) -> list[int]:

        # first convert the input into an integer
        total = 0
        powerOf = len(digits) - 1
        for i in digits:
            total += i * (10 ** powerOf)
            powerOf -= 1
        # add +1 to the sum and then convert that to a list
        return [int(digit) for digit in str(total + 1)]

