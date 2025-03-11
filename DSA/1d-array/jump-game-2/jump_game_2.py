#https://leetcode.com/problems/jump-game-ii/description/?envType=problem-list-v2&envId=array

# This is same as Jump Game only but there will be True cases only.
class JumpGame2:
    def jump(self, nums: list[int]) -> int:
        length = len(nums)
        i = 0
        # returning 0 means, no such jumps available which should ideally not happen as per the problem statement.
        count = 1
        if length > 2:
            while i <= length - 2: #ignore the last index
                if nums[i] == 0: #no more jumping possible
                    return 0
                cMax = i + nums[i]
                newI = i
                if cMax >= length - 1: # as i is 0 based
                    break
                for j in range(i+1, min(length - 1, i+nums[i]+1)): #exclude last index
                    nMax = j + nums[j]
                    if nMax > cMax:
                        cMax = nMax
                        newI = j
                
                if i == newI:
                    return 0 # avoid infinite loop
                else: 
                    i = newI
                    count += 1
        else:
            if length == 1:
                count = 0
            elif length == 2 and nums[0] > 0:
                count = 1
        return count
