class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the column target
        m = len(matrix)
        lo_col, hi_col = 0, m - 1

        # find the col
        target_m = -1
        while lo_col <= hi_col:
            mid = (lo_col + hi_col) // 2
            if matrix[mid][0] <= target: # if target is more than min_col
                target_m = mid
                lo_col = mid + 1
            else:
                hi_col = mid - 1
        if target_m == -1:
            return False
        # find the row
        target_row = matrix[target_m]
        n = len(target_row)
        lo_row, hi_row = 0, n - 1
        while lo_row <= hi_row:
            mid_row = (lo_row + hi_row) // 2
            if target_row[mid_row] == target:
                return True
            elif target_row[mid_row] < target:
                lo_row = mid_row + 1
            else:
                hi_row = mid_row - 1
        return False
