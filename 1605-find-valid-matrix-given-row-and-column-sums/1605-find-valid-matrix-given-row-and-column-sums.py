class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows, cols = len(rowSum), len(colSum)
        res = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            res[r][0] = rowSum[r]
        
        for c in range(cols):
            cur_col_sum = 0
            for r in range(rows):
                cur_col_sum += res[r][c]
        
            r = 0
            while cur_col_sum > colSum[c]:
                diff = cur_col_sum - colSum[c]
                max_shift = min(res[r][c], diff)
                res[r][c] -= max_shift
                res[r][c+1] = max_shift
                cur_col_sum -= max_shift
                r += 1
        return res