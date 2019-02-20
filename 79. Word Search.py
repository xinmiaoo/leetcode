class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(m,n,idx):
            if m<0 or n<0 or m==len(board) or n==len(board[0]) or board[m][n]!=word[idx]:
                return False
            if idx==len(word)-1:
                return True
            board[m][n]='*'
            TF=dfs(m-1,n,idx+1) or dfs(m+1,n,idx+1) or dfs(m,n-1,idx+1) or dfs(m,n+1,idx+1)
            board[m][n]=word[idx]
            return TF
        
        if word==[]:
            return True
        h,w=len(board),len(board[0])
        rs=False
        for i in range(h):
            for j in range(w):
                rs=rs or dfs(i,j,0)
                
        return rs
