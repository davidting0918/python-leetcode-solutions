# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/description/?envType=daily-question&envId=2025-01-12
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # use stack to solve this question,
        # solution logic:
        # 1. Only one condition need to early return False: there is a locked ")" without a locked "(" or open "(" before it.
        # 2. no matter locked or unlocked "(", we need to push it to the stack but in different stacks since locked has higher priority.

        n = len(s)

        if n % 2 != 0:
            return False

        locked_left = []
        unlocked = []

        for i in range(n):

            if locked[i] == '0':
                unlocked.append(i)
            elif s[i] == "(":
                locked_left.append(i)
            elif s[i] == ")":
                if locked_left:
                    locked_left.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False
        while locked_left and unlocked:
            if locked_left[-1] < unlocked[-1]:
                locked_left.pop()
                unlocked.pop()
            else:
                break

        return not locked_left

if __name__ == '__main__':
    s = Solution()
    string = "())(()(()(())()())(())((())(()())((())))))(((((((())(()))))("
    locked = "100011110110011011010111100111011101111110000101001101001111"
    print(s.canBeValid(string, locked)) # True