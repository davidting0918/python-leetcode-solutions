# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
class Solution:
    def minAddToMakeValid_1(self, s: str) -> int:
        # use string sum to solve the question
        string_sum = 0
        add_time = 0
        for i in s:
            if i == '(':
                string_sum += 1
            elif i == ')':
                string_sum -= 1
            if string_sum < 0:
                add_time += 1
                string_sum += 1
        return add_time + string_sum

    def minAddToMakeValid_2(self, s: str) -> int:
        # use stack to solve the question
        stack = []
        for i in s:
            if i == '(':
                stack.append(i)
            elif i == ')' and stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
        return len(stack)

if __name__ == "__main__":
    s = Solution()
    print(s.minAddToMakeValid_1('()))(('))  # 4