class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=0
        i=0

        while i < len(nums):
            if nums[k] != nums[i]:
                k = k+1
                nums[k] = nums[i]
            i += 1
        return k+1