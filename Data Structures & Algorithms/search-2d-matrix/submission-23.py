class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        col_matrix = [m[0] for m in matrix]
        print(f"col_matrix: {col_matrix}")
        lo_col, hi_col = 0, m - 1
        print(f"lo_col, hi_col: {lo_col}, {hi_col}")
        target_row = -1
        while lo_col <= hi_col:
            mid_col = (lo_col + hi_col) // 2
            if target >= col_matrix[mid_col]:
                target_row = mid_col
                # next lo_col
                lo_col = mid_col + 1
            else:
                hi_col = mid_col - 1
        print(f"target_row = {target_row}")
        if target_row == -1:
            return False
        target_list = matrix[target_row]
        low_e , high_e = 0 , n - 1
        while low_e <= high_e:
            mid_e = (low_e + high_e) // 2
            if target_list[mid_e] == target:
                return True
            elif target > target_list[mid_e]:
                low_e = mid_e + 1
            else:
                high_e = mid_e - 1
        return False
        

        # [1, 10, 14]
        # if the number is 15
            # 15 > 10
            # mid_col = 10 
            # lo_col = mid_col
        # if the number is 3
            # 3 < 10 
            # hi_col = 1
            # mid_col = 0 
            # 