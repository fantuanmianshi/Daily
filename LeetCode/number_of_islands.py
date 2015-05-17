"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of
islands. An island is surrounded by water and is formed by connecting adjacent
lands horizontally or vertically. You may assume all four edges of the grid are
all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3

Tags: DFS, BFS

Difficulty: Medium
"""


class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        if not grid:
            return 0
        if not grid[0]:
            return 0

        width = len(grid[0])
        height = len(grid)
        visited = [[False] * width for _ in xrange(height)]

        count = 0
        i = 0
        while i < height:
            j = 0
            while j < width:
                if grid[i][j] == '1' and not visited[i][j]:
                    self.bfs(grid, visited, [(i, j)])
                    count += 1
                j += 1
            i += 1
        return count


    def bfs(self, grid, visited, to_be_visited):
        if not to_be_visited:
            return

        x, y = to_be_visited.pop()
        if visited[x][y] or grid[x][y] == '0':
            return
        visited[x][y] = True

        if x > 0:
            to_be_visited.append((x - 1, y))
        if x < len(visited) - 1:
            to_be_visited.append((x + 1, y))
        if y > 0:
            to_be_visited.append((x, y - 1))
        if y < len(visited[0]) - 1:
            to_be_visited.append((x, y + 1))

        while to_be_visited:
            self.bfs(grid, visited, to_be_visited)
