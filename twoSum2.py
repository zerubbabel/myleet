# one-pass hash table
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_tbl={}
        for i in range(len(nums)):
            c=target-nums[i]
            if c in hash_tbl:
                return [hash_tbl[c],i]
            else:
                hash_tbl[nums[i]]=i