from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = {}

        for i in nums:
            cnt[i] = cnt.get(i, 0) + 1

        answer = 0
        for i in cnt:
            target = k - i
            if target in cnt:
                answer += min(cnt[i], cnt[target])
        return answer // 2

if __name__ == "__main__":
    s = Solution()
    print(s.maxOperations([1,2,3,4], 5))