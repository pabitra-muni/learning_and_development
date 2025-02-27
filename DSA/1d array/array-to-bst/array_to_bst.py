class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ArrayToBst:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:

        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
         # above 2 create array subsets each time and hence takes more memory adding to space compexity

        return root;
    
    # Below function doesn't create subsets, rather acts on the original array and hence keepting 
    # time complexity at O(1)

    def sortedArrayToBST_Optimized(self, nums: list[int]) -> TreeNode:
        return self.__helper(nums, 0, len(nums))

    def __helper(self, nums: list[int], left: int, right: int) -> TreeNode:
        if left >= right:
            return None
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = self.__helper(nums, left, mid)
        root.right = self.__helper(nums, mid + 1, right)
        return root