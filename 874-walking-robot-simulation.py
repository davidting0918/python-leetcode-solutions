# https://leetcode.com/problems/walking-robot-simulation/description/?envType=daily-question&envId=2024-09-04
from typing import List
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0
        x, y = 0, 0
        
        farest = 0
        for i in commands:
            if i == -2:
                dir_idx -=1
            elif i == -1:
                dir_idx += 1
            else:
                for j in range(i):
                    x += directions[dir_idx][0]
                    y += directions[dir_idx][1]
                    if [x, y] in obstacles:
                        x -= directions[dir_idx][0]
                        y -= directions[dir_idx][1]
                        break
                    if x*x + y*y < farest:
                        break
                    farest = x*x + y*y
        return farest
        
    

if __name__ == "__main__":
    s = Solution()
    print(s.robotSim([4,-1,3], []))