import pytest
from array_to_bst import ArrayToBst, TreeNode

@pytest.mark.parametrize(
    "nums",
    [
        ([-10,-3,0,5,9]),
        ([1,3])
    ]
)
def test_merge(nums):
    actual = ArrayToBst().sortedArrayToBST_Optimized(nums)
    final_result = []
    inorder_traversal(actual, final_result)
    assert final_result == nums
    assert is_balanced(actual) == True

def inorder_traversal(root: TreeNode, result: list[int]):
    if root:
        inorder_traversal(root.left, result)
        result.append(root.val)
        inorder_traversal(root.right, result)

def check_height(root):
    """Returns the height of the tree if balanced, otherwise -1."""
    if root is None:
        return 0  # Base case: Height of an empty tree is 0

    left_height = check_height(root.left)
    if left_height == -1:
        return -1  # Left subtree is unbalanced
    
    right_height = check_height(root.right)
    if right_height == -1:
        return -1  # Right subtree is unbalanced
    
    if abs(left_height - right_height) > 1:
        return -1  # If height difference > 1, tree is unbalanced

    return max(left_height, right_height) + 1  # Return height of current node

def is_balanced(root: TreeNode) -> bool:
    """Returns True if the BST is balanced, otherwise False."""
    return check_height(root) != -1