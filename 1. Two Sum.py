class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for index, n in enumerate(nums):
            if dic.get(target - n) != None:
                return [dic.get(target - n), index]
            else:
                dic[n] = index

        return None


solution = Solution()
result = solution.twoSum([2, 7, 11, 15], 9)
print(result)