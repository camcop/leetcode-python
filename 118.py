class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for n in range(1, numRows + 1):
            row = []

            if n == 1:
                row = [1]
            else:
                previous_row = triangle[n - 2]
                for m in range(n):               
                    if m == 0 or m == n - 1:
                        row.append(1)
                    else:
                        row.append(previous_row[m - 1] + previous_row[m])
            triangle.append(row)

        return triangle


