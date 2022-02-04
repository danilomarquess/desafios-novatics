class Solution(object):
    def ValidacaoSudoku(self, sudoku):
        for i in range(9):
            linha = {}
            coluna = {}
            bloco = {}
            linha_cubo = 3 * (i // 3)
            coluna_cubo = 3 * (i % 3)
            for j in range(9):
                if sudoku[i][j] != "." and sudoku[i][j] in linha:
                    return False
                linha[sudoku[i][j]] = 1
                if sudoku[j][i] != "." and sudoku[j][i] in coluna:
                    return False
                coluna[sudoku[j][i]] = 1
                lc = linha_cubo + j // 3
                cc = coluna_cubo + j % 3
                if sudoku[lc][cc] in bloco and sudoku[lc][cc] != ".":
                    return False
                bloco[sudoku[lc][cc]] = 1
        return True


teste = Solution()
print(teste.ValidacaoSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."] #output = True
                        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

print(teste.ValidacaoSudoku([["8","3",".",".","7",".",".",".","."] #output = False
                        ,["6",".",".","1","9","5",".",".","."]
                        ,[".","9","8",".",".",".",".","6","."]
                        ,["8",".",".",".","6",".",".",".","3"]
                        ,["4",".",".","8",".","3",".",".","1"]
                        ,["7",".",".",".","2",".",".",".","6"]
                        ,[".","6",".",".",".",".","2","8","."]
                        ,[".",".",".","4","1","9",".",".","5"]
                        ,[".",".",".",".","8",".",".","7","9"]]))