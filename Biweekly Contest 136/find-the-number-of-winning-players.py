# https://leetcode.com/contest/biweekly-contest-136/problems/find-the-number-of-winning-players/description/

class Solution:
    def winningPlayerCount(self, n: int, pick: list[list[int]]) -> int:
        ht = {
            i: {} for i in range(n)
        }
        winners = []
        result = 0
        for p in pick:
            ht[p[0]][p[1]] = ht[p[0]].get(p[1], 0) + 1

            if ht[p[0]][p[1]] > p[0] and p[0] not in winners:
                winners.append(p[0])
                result += 1

        return result

if __name__ == "__main__":
    s = Solution()
    n = 4
    pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]
    print(s.winningPlayerCount(n, pick))

    n = 5
    pick = [[1,1],[1,2],[1,3],[1,4]]
    print(s.winningPlayerCount(n, pick))

    n = 5
    pick = [[1,1],[2,4],[2,4],[2,4]]
    print(s.winningPlayerCount(n, pick))