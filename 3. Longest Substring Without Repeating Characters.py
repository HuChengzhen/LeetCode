class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        length = 1
        start = 0
        charAtIndex ={}
        for index in range(len(s)):
            char_at = charAtIndex.get(s[index])
            if char_at is not None:
                start = max(char_at + 1, start)
            length = max(length, index - start + 1)
            charAtIndex[s[index]] = index
        return length


solution = Solution()
print(solution.lengthOfLongestSubstring("tmmzuxt"))
print(solution.lengthOfLongestSubstring("au"))