#https://leetcode.com/problems/jump-game/?envType=problem-list-v2&envId=array

class JumpGame:
    def canJump(self, nums: list[int]) -> bool:
        length = len(nums)
        i = 0
        if length > 2:
            while i <= length - 2: #ignore the last index
                if nums[i] == 0: #no more jumping possible
                    return False
                cMax = i + nums[i]
                newI = i
                if cMax >= length - 1: # as i is 0 based
                    return True
                for j in range(i+1, min(length - 1, i+nums[i]+1)): #exclude last index
                    nMax = j + nums[j]
                    if nMax > cMax:
                        cMax = nMax
                        newI = j
                
                if i == newI:
                    return False # avoid infinite loop
                else: 
                    i = newI
        else:
            return length == 1 or (length == 2 and nums[0] > 0)
        return False

