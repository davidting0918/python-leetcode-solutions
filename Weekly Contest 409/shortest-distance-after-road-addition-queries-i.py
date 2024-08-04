# https://leetcode.com/contest/weekly-contest-409/problems/shortest-distance-after-road-addition-queries-i/description/
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        paths = {
            i: [i + 1] for i in range(n - 1)
        }
        results = []
        for q in queries:
            paths[q[0]].append(q[1])

            step = 0
            current = 0
            while current < n - 1:
                step += 1
                current = max(paths[current])
            results.append(step)

        return results

if __name__ == "__main__":
    s = Solution()
    # n = 5
    # queries = [[2,4],[0,2],[0,4]]
    # print(s.shortestDistanceAfterQueries(n, queries))
    #
    # n = 5
    # queries = [[1,3],[2,4]]
    # print(s.shortestDistanceAfterQueries(n, queries))
    #
    n = 6
    queries = [[1,4],[0,2]]
    print(s.shortestDistanceAfterQueries(n, queries))