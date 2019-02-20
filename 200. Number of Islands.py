class Solution(object):
  def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid or not grid[0]:
        return 0

    def dfs(grid,i,j):
      grid[i][j]='0'
      if i>0 and grid[i-1][j]=='1':
        dfs(grid,i-1,j)
      if i<len(grid)-1 and grid[i+1][j]=='1':
        dfs(grid,i+1,j)
      if j>0 and grid[i][j-1]=='1':
        dfs(grid,i,j-1)
      if j<len(grid[0])-1 and grid[i][j+1]=='1':
        dfs(grid,i,j+1)


    nums_island = 0
    w, h = len(grid), len(grid[0])
    for m in range(w):
      for n in range(h):
        if grid[m][n] == '1':
            dfs(grid,m,n)
            nums_island += 1

    return nums_island




'''
class Solution(object):
  def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if grid==[]:
        return 0
    def dfs(i, j, l):
      if i < 0 or i >=len(grid) or j < 0 or j >=len(grid[0]) or grid[i][j] == '0':
        return set()
      l.add((i, j))
      if (i - 1, j) not in l:
        l = l.union(dfs(i - 1, j, l))
      if (i +1, j) not in l:
        l = l.union(dfs(i+1, j, l))
      if (i , j+1) not in l:
        l = l.union( dfs(i , j+1, l))
      if (i , j-1) not in l:
        l = l.union( dfs(i , j-1, l))
      return l

    nums_island = 0
    w, h = len(grid), len(grid[0])
    l = set()
    for m in range(w):
      for n in range(h):
        if grid[m][n] == '1':
          if (m, n) not in l:
            l = l.union(dfs(m, n, l))
            nums_island += 1

    return nums_island

  ##but got Time Limit Exceeded###
'''
