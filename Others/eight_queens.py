"""
输出N皇后解的数量。

样例输入：4

样例输出：2
"""

class Solution1:
    total = 0

    def search(cur, N, C):
        '''
        cur: how many queens have been placed
        N: the number of total queens
        C: solution array
        '''
        if cur == N:
            global total
            # print C 
            total += 1
        else:
            for i in range(0, N):
                ok = True
                C[cur] = i
                for j in range(0, cur):
                    if C[cur] == C[j] \
                       or cur-C[cur] == j - C[j] \
                       or cur+C[cur] == j + C[j]:
                        ok = False
                        break
                if ok:
                    search(cur+1, N, C)

    def n_queens(N):
        search(0, N, [0] * N)
        global total
        print total
        
    n_queens(8)


class Solution2:
    def can_attack(row, columnsForRow):
    for i in range(row):
        if columnsForRow[i] == columnsForRow[row] or \
           abs(columnsForRow[row] - columnsForRow[i]) == row - i:
            return True
    return False


    def n_queens(n, row, columnsForRow):
        count = 0
        if row == n:
            return 1
        else:
        col = 0
        while col < n:
            columnsForRow[row] = col
            if not can_attack(row, columnsForRow):
            count += n_queens(n, row + 1, columnsForRow)
            col += 1
        return count


    if __name__ == '__main__':
        print n_queens(4, 0, [None] * 4)
        print n_queens(8, 0, [None] * 8)
 