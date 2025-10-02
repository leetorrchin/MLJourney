class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        seen = set()
        while i < len(nums):
            if nums[i] in seen:
                nums.pop(i)
            else:
                seen.add(nums[i])
                i += 1
        return len(nums)