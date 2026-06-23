class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        len_rows = len(grid)
        len_col = len(grid[0])
        def search_islands(cur_row,cur_col):
            if cur_row < 0 or cur_row >= len_rows or cur_col < 0 or cur_col >=len_col or grid[cur_row][cur_col] == "0":
                return
            grid[cur_row][cur_col] = "0"
            search_islands(cur_row,cur_col-1)
            search_islands(cur_row-1,cur_col)
            search_islands(cur_row+1,cur_col)
            search_islands(cur_row,cur_col+1)
        count = 0
        for r in range(0,len_rows):
            for c in range(0,len_col):
                if grid[r][c] == "1":
                    search_islands(r,c)
                    count+=1
        return count