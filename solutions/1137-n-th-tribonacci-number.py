# https://leetcode.com/problems/n-th-tribonacci-number/description/?envType=study-plan-v2&envId=dynamic-programming
from typing import List
class Solution:
    def tribonacci(self, n: int) -> int:
        fib_list = [0, 1, 1]

        if n < 3:
            return fib_list[n]
        
        for i in range(2, n):
            fib_list.append(fib_list[i] + fib_list[i-1] + fib_list[i-2])
        
        return fib_list[n]