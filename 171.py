class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        # vals = [ord(c) - 64 for c in columnTitle]

        # val = 0
        # for i, n in enumerate(vals[::-1]):
        #     val += n * 26**i
        # return val

        return sum([(ord(c) - 64) * 26**i for i, c in enumerate(columnTitle[::-1])])