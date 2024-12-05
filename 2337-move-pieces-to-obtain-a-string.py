# https://leetcode.com/problems/move-pieces-to-obtain-a-string/description/?envType=daily-question&envId=2024-12-05
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace("_", "") != target.replace("_", ""):
            return False

        start_index = 0
        target_index = 0
        n = len(start)

        while start_index < n and target_index < n:
            while start_index < n and start[start_index] == "_":
                start_index += 1
            while target_index < n and target[target_index] == "_":
                target_index += 1

            if start_index == n or target_index == n:
                break

            if start[start_index] == "L" and start_index < target_index:
                return False
            if start[start_index] == "R" and start_index > target_index:
                return False

            start_index += 1
            target_index += 1
        return True


if __name__ == "__main__":
    s = Solution()
    start = "R______RR"
    target = "___R___RR"
    print(s.canChange(start, target)) # True