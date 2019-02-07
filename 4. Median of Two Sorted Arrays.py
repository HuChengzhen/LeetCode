class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = nums1 + nums2  # type: list
        nums3.sort()

        length = len(nums3)
        if length % 2 == 0:
            return (nums3[length // 2 - 1] + nums3[length // 2]) / 2
        else:
            return nums3[length // 2]
