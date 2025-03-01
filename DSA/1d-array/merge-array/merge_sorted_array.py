# https://leetcode.com/problems/merge-sorted-array/description/?envType=problem-list-v2&envId=array

"""

initialize three pointers, 'p1', 'p2', and 'pMerge', where 'p1' and 'p2' point to the last valid elements
in nums1 and nums2, respectively. 'pMerge' will point to the last available position in nums1. 
Then start from the end of both arrays and compare elements at 'p1' and 'p2'. Place the larger element at 'pMerge' 
and decrement the corresponding pointers and 'pMerge'. Continue this process until all elements from nums2 are merged into nums1.

"""


class MergeArray:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None: 
        p1 = m - 1;
        p2 = n - 1;
        pMerge = m + n - 1;
        
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[pMerge] = nums1[p1]
                pMerge -= 1
                p1 -= 1
            else:
                nums1[pMerge] = nums2[p2]
                pMerge -= 1
                p2 -= 1
        