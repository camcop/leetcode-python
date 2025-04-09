class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        word = str(x)        
        # if odd length remove middle char from string
        if len(word) % 2 == 1:
            word = word[:len(word) // 2] + word[len(word) // 2 + 1:]


        iteration = 0
        mid = int(len(word) / 2)
        for i in range(mid, len(word)):
            iteration += 1
            if word[i] != word[mid - (1 * iteration)]:
                return False
        return True


# print(Solution().isPalindrome(121))
# print(Solution().isPalindrome(10))
print(Solution().isPalindrome(1001))