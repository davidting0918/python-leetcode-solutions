# https://leetcode.com/problems/combination-sum-ii/description/?envType=daily-question&envId=2024-08-13
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start: int, target: int, path: List[int]):
            # Use recursion to find the path

            if target == 0:
                if path not in results:
                    results.append(path[:])
                return
            elif target < 0:
                return
            else:
                for i in range(start, n):
                    if i > start and sorted_nums[i] == sorted_nums[i - 1]:  # ignore the same number since have dealt with it in the previous iteration
                        continue 
                    if sorted_nums[i] > target:
                        break

                    path.append(sorted_nums[i])
                    # print(f"Start finding path with: {path} at index {i}")
                    backtrack(i+1, target - sorted_nums[i], path)
                    path.pop()
        
        
        n = len(candidates)
        sorted_nums = sorted(candidates)

        results = []

        if sum(candidates) < target:
            return results
        if sum(candidates) == target:
            return [candidates]

        print(sorted_nums)
        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            if sorted_nums[i] > target:
                break
            path = [sorted_nums[i]]
            
            print(f"Start finding path with: {path} at index {i}")
            backtrack(i+1, target - sorted_nums[i], path)
        return results
    

if __name__ == "__main__":
    s = Solution()
    candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    target = 30
    print(s.combinationSum2(candidates, target))