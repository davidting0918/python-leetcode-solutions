# python-leetcode-solutions
This is a place to store all the leetcode solutions from every day exercise

### Table of Content
- [DP](#dp)
- [Graph](#graph)
- [Hash Table](#hash-table)



### DP
#### Great Question
- [2779. Maximum Beauty of an Array After Applying Operation](https://github.com/davidting0918/python-leetcode-solutions/blob/master/solutions/2779-maximum-beauty-of-an-array-after-applying-operation.py)  
Solution logic: Use sweep line to calculate the sum of the subarray, and then use the sum to calculate the beauty of the subarray.

- [1769. Minimum Number of Operations to Move All Balls to Each Box](https://github.com/davidting0918/python-leetcode-solutions/blob/master/solutions/1769-minimum-number-of-operations-to-move-all-balls-to-each-box.py)  
Solution logic:  
  1. Declare `prefix_sum` and `suffix_sum`, which are two list to store the total step to move the balls lefter and righter to the current index.
  2. Take `prefix_sum` as an example, will declare `ball_count` to store the total balls number lefter than the current index. 
  Use `prefix_sum[i] = prefix_sum[i-1] + ball_count` to calculate the total steps to move the balls lefter to the current index.
  3. Answer will be the sum of `prefix_sum` and `suffix_sum`.


### Graph
#### Great Question
- [207. Course Schedule](https://github.com/davidting0918/python-leetcode-solutions/blob/master/soltuions/207-course-schedule.py)  
Solution logic:
  1. First declare two variables, `graph` and `in_degree`. `graph` is a list of list, `graph[i]` stores all the courses can be taken after finished course `i`. `in_degree` is a list of int, `in_degree[i]` stores the number of courses that need to be taken before taking course `i`. 
  2. Then declare `queue` and `count`. `queue` is a list of int, `queue` stores the courses that can be taken now. `count` is an int, `count` stores the number of courses that can be taken now.
  3. Each time we take a course from `queue`, we decrease the `in_degree` of the courses that can be taken after this course. If the `in_degree` of the course is 0, we add this course to the `queue`.
  4. Finally, we check if the `count` is equal to the number of courses. If it is, return `True`, otherwise return `False`.


- [994. Rotting Oranges](https://github.com/davidting0918/python-leetcode-solutions/blob/master/solutions/994-rotting-oranges.py)  
Solution logic:
  1. use BFS to traverse the grid, since need to get the minutes, we need to store the minutes in the grid.
  2. declare `queue` and `fresh_oranges`. `queue` is a list of tuple, `queue` stores the position of the rotten oranges (as the starting point if rotting). `fresh_oranges` is an int, `fresh_oranges` stores the number of fresh oranges.
  3. return `-1` if there is still fresh oranges after the BFS, otherwise return the maximum minutes in the grid.


### Hash Table
#### Great Question
- [1930. Unique Length-3 Palindromic Subsequences](https://github.com/davidting0918/python-leetcode-solutions/blob/master/solutions/1930-unique-length-3-palindromic-subsequences.py)  
Solution logic:
  1. First declare `letters` which is a set of the given string.
  2. Since the length of valid substring must be 3, the first and last letter must be the same.
  3. Then we iterate through the `letters` to check whether the `letter` occur twice (remember their index `left`, `right`).
  4. Then iterate through the `letters` second time to check if the letter appear between `left` and `right`. if it does, `ans` plus 1.
