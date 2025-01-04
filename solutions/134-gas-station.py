# https://leetcode.com/problems/gas-station/description/
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        # then must have a solution
        current_tank = 0
        start_index = 0
        for i in range(len(gas)):
            current_tank += gas[i] - cost[i]
            if current_tank < 0:  # then this index can't be the start index, must start from the next index
                current_tank = 0
                start_index = i + 1
        
        return start_index
    
if __name__ == "__main__":
    s = Solution()
    
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    print(s.canCompleteCircuit(gas, cost))
