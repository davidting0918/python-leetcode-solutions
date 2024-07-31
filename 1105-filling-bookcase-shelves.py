# https://leetcode.com/problems/filling-bookcase-shelves/description/
class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        

        for end in range(n):
            width = 0
            height = 0
            for start in range(end, -1, -1):
                # assume put books[start:end + 1] on the same shelf
                width += books[start][0]
                if width > shelfWidth:
                    break
                height = max(height, books[start][1])
                dp[end + 1] = min(dp[end + 1], dp[start] + height)
                print(f"Start: {start}, End: {end}, Width: {width}, Height: {height}, DP: {dp}")

        return dp[n]
    

if __name__ == "__main__":
    s = Solution()

    books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
    shelf_width = 4
    print(s.minHeightShelves(books, shelf_width))