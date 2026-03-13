# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
"""
84. Largest Rectangle in Histogram (Hard)

Given an array of integers heights representing the histogram's bar heights
(each bar has width 1), find the area of the largest rectangle in the histogram.

Approach: Monotonic Stack
- Maintain a stack of indices with non-decreasing heights.
- When we encounter a bar shorter than the stack top, pop and calculate
  the area using the popped bar as the shortest bar in the rectangle.
- The width extends from the new stack top + 1 to the current index - 1.
- Append a sentinel height of 0 to flush remaining bars at the end.
- Time: O(n) — each bar is pushed and popped at most once
- Space: O(n) for the stack
"""


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack: list[int] = []  # stack of indices
        max_area = 0
        # Append 0 as sentinel to force all remaining bars to be processed
        heights.append(0)

        for i, h in enumerate(heights):
            # Pop bars taller than current — they can't extend further right
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                # Width: from (stack top + 1) to (i - 1)
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        heights.pop()  # restore original list
        return max_area
