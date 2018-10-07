class Solution(object):

	def twoSum(self, nums, target):
		"""
		type nums: List[int]
		type target: int
		rtype: List[int]
		"""
		hash_map = {}
        for index, value in enumerate(nums):
            hash_map[value] = index
        for index1, value in enumerate(nums):
            if target - value in hash_map:
                index2 = hash_map[target - value]
                if index1 != index2:
                    return [index1 + 1, index2 + 1]