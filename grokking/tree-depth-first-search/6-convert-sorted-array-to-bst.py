# input sorted array
# output: bst

# init mid to round(len(array))
# init low to 0
# init high to len(array)

from utils import TreeNode

def sorted_array_to_bst_helper(nums, low, high):
    if( low > high):
        return None

    mid = low +(high-low)//2
    root = TreeNode(nums[mid])

    root.left = sorted_array_to_bst_helper(nums, low, mid-1)
    root.right = sorted_array_to_bst_helper(nums, mid+1, high)

    return root


def sorted_array_to_bst(nums):
    return sorted_array_to_bst_helper(nums, 0, len(nums) - 1)
