class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        def dfs(i,j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!=1:
                return 0
            
            grid[i][j]=0
            return dfs(i-1,j)+dfs(i,j-1)+dfs(i+1,j)+dfs(i,j+1)+1
            
        
        
        h,w=len(grid),len(grid[0])
        
        max_area=0
        for i in range(h):
            for j in range(w):
                max_area=max(max_area,dfs(i,j))
                
                
        return max_area
    
    
        
