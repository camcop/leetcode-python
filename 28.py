class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        for i, c in enumerate(haystack):
            for j, x in enumerate(needle):
                if i + j == len(haystack):
                    return -1
                if haystack[i + j] != x:
                    break
                if j == len(needle) - 1:
                    return i
        return -1
        

sol = Solution()
print(sol.strStr("leetcode", "leeto"))

"""
Can of course use Python builtin .index() but that's kind of cheating
"""