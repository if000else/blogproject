an = [1,1,3]
# an.pop(4)
# print(an)
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        l = len(nums)
        while i < l:
        	for j in range(i):
        		if nums[i] == nums[j]:
        			nums.pop(i)
        			l = len(nums)
        		else:
        			i += 1
        		
a = Solution()
print(a.removeDuplicates(an))