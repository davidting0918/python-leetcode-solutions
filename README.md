# python-leetcode-solutions
This is a place to store all the leetcode solutions from every day exercise

### Table of Content
- [DP](#dp)
- [Graph](#graph)



### DP
#### Great Question
- [2779. Maximum Beauty of an Array After Applying Operation](https://github.com/davidting0918/python-leetcode-solutions/blob/master/2779-maximum-beauty-of-an-array-after-applying-operation.py)  
Solution logic: Use sweep line to calculate the sum of the subarray, and then use the sum to calculate the beauty of the subarray.


### Graph
#### Great Question
- [207. Course Schedule](https://github.com/davidting0918/python-leetcode-solutions/blob/master/207-course-schedule.py)  
Solution logic:
  1. First declare two variables, `graph` and `in_degree`. `graph` is a list of list, `graph[i]` stores all the courses can be taken after finished course `i`. `in_degree` is a list of int, `in_degree[i]` stores the number of courses that need to be taken before taking course `i`. 
  2. Then declare `queue` and `count`. `queue` is a list of int, `queue` stores the courses that can be taken now. `count` is an int, `count` stores the number of courses that can be taken now.
  3. Each time we take a course from `queue`, we decrease the `in_degree` of the courses that can be taken after this course. If the `in_degree` of the course is 0, we add this course to the `queue`.
  4. Finally, we check if the `count` is equal to the number of courses. If it is, return `True`, otherwise return `False`.


- [994. Rotting Oranges](httpshttps://github.com/davidting0918/python-leetcode-solutions/blob/master/994-rotting-oranges.py)  
Solution logic:
  1. use BFS to traverse the grid, since need to get the minutes, we need to store the minutes in the grid.
  2. declare `queue` and `fresh_oranges`. `queue` is a list of tuple, `queue` stores the position of the rotten oranges (as the starting point if rotting). `fresh_oranges` is an int, `fresh_oranges` stores the number of fresh oranges.
  3. return `-1` if there is still fresh oranges after the BFS, otherwise return the maximum minutes in the grid.