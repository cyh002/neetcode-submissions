class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        min_col = [row[0] for row in matrix]
        # find the column target
        m = len(min_col)
        lo_col, hi_col = 0, m - 1
        
        # find the col
        target_m = -1
        while lo_col <= hi_col:
            mid = (lo_col + hi_col) // 2
            if min_col[mid] <= target: # if target is more than min_col
                target_m = mid
                lo_col = mid + 1
            else:
                hi_col = mid - 1
        
        # find the row
        target_row = matrix[target_m]
        n = len(target_row)
        lo_row, hi_row = 0, n - 1
        while lo_row <= hi_row:
            mid_row = (lo_row + hi_row) // 2
            if target_row[mid_row] == target:
                return True
            elif target_row[mid_row] < target:
                lo_row += 1
            else:
                hi_row -= 1
        return False
