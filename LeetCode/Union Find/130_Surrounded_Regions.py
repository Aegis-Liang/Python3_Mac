# it's not god for use union find?

class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board == []:
            return
        # print(board)
        UF = UnionFind(board)
        UF.walkThroughBoard()
        UF.rewriteBoard()
        board = UF.board
        print(UF.board)

        """
        print(UF.rowCount)
        UF.union(15, 16)
        print(UF.id)
        print(UF.sz)
        print(UF.root(16))
        print(UF.root(15))
        print(UF.getOorX(6))
        print(UF.getOorX(7))
        """


class UnionFind:
    def __init__(self, board):
        self.board = board
        self.rowCount = len(self.board)
        self.colCount = len(self.board[0])
        self.sz = [1] * (self.rowCount * self.colCount + 1)
        self.id = [i * self.colCount + j for i in range(self.rowCount) for j in range(self.colCount)] # the fisrt variable is colCount not rowCount
        self.id.append(self.rowCount * self.colCount)  # for simplification, use total number instead of -1

    def root(self, p):
        while self.id[p] != p:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p

    def isConnected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if self.sz[i] > self.sz[j]:
            self.id[j] = i
            self.sz[i] += self.sz[j]  # the assigned variable of this line is different from last line, should take care
        else:
            self.id[i] = j
            self.sz[j] += self.sz[i]

    def walkThroughBoard(self):
        for i in range(self.rowCount * self.colCount):
            row = i // self.colCount
            col = i % self.colCount
            if self.board[row][col] == "O":
                # print("i:%d row:%d col:%d", i, row, col)
                if row == 0:
                    self.unionWithPointType(i, "last")  # union last
                else:
                    if row != self.rowCount - 1:    # need to minus 1 because row is an index from 0
                        self.unionWithPointType(i, "below")  # union below

                if row == self.rowCount - 1:
                    self.unionWithPointType(i, "last")  # union last
                else:
                    if row != 0:
                        self.unionWithPointType(i, "above")  # union above

                if col == 0:
                    self.unionWithPointType(i, "last")  # union last
                else:
                    if col != self.colCount - 1:
                        self.unionWithPointType(i, "right")  # union right

                if col == self.colCount - 1:
                    self.unionWithPointType(i, "last")  # union last
                else:
                    if col != 0:
                        self.unionWithPointType(i, "left")  # union left

    def rewriteBoard(self):
        totalNumber = self.rowCount * self.colCount
        for i in range(totalNumber):
            row = i // self.colCount
            col = i % self.colCount
            if not self.isConnected(i, totalNumber):
                self.board[row][col] = "X"

    def getOorX(self, p):
        return self.board[p // self.colCount][p % self.colCount]

    def unionWithPointType(self, p, pointType):
        if pointType == "last":
            self.union(p, self.rowCount * self.colCount)
        if pointType == "left":
            if self.getOorX(p - 1) == "O":
                self.union(p, p - 1)
        if pointType == "right":
            if self.getOorX(p + 1) == "O":
                self.union(p, p + 1)
        if pointType == "above":
            if self.getOorX(p - self.colCount) == "O":
                self.union(p, p - self.colCount)
        if pointType == "below":
            if self.getOorX(p + self.colCount) == "O":
                self.union(p, p + self.colCount)

if __name__ == "__main__":
    Solution.solve(Solution, [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']])
    # Solution.solve(Solution, [])
    # Solution.solve(Solution, [["X", "O", "X", "X"], ["O", "X", "O", "X"], ["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"], ["O", "X", "O", "X"]])









