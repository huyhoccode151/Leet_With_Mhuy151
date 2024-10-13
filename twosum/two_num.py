class Solution(object):
    def twoSum(self, nums, target):
        num_dict = {}
        for key,val in enumerate(nums):
            b = target - val
            if b in num_dict:
                return [num_dict[b], key]
            num_dict[val] = key
        return None


# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]