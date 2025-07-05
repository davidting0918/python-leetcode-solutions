# https://leetcode.com/contest/biweekly-contest-160/problems/minimum-cost-path-with-alternating-directions-ii/description/
from typing import List
import heapq

class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:        
        def get_entry_cost(i: int, j: int) -> int:
            return (i + 1) * (j + 1)
        
        heap = [
            (get_entry_cost(0, 0), 0, 0, 1)  # (cost, i, j, second)
        ]

        visited = [[[float('inf')] * 2 for _ in range(n)] for _ in range(m)]
        visited[0][0][1] = get_entry_cost(0, 0)

        while heap:
            cost, x, y, time = heapq.heappop(heap)
            
            if x == m - 1 and y == n - 1:
                return cost  # 抵達終點
            
            parity = time % 2
            
            if visited[x][y][parity] < cost:
                continue
            
            if parity == 1:
                for dx, dy in [(0, 1), (1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        ncost = cost + get_entry_cost(nx, ny)
                        if visited[nx][ny][(time+1)%2] > ncost:
                            visited[nx][ny][(time+1)%2] = ncost
                            heapq.heappush(heap, (ncost, nx, ny, time + 1))
            else:
                ncost = cost + waitCost[x][y]
                if visited[x][y][(time+1)%2] > ncost:
                    visited[x][y][(time+1)%2] = ncost
                    heapq.heappush(heap, (ncost, x, y, time + 1))

if __name__ == "__main__":
    s = Solution()
    m = 1
    n = 2
    waitCost = [[1,2]]
    print(s.minCost(m, n, waitCost))