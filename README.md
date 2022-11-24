# adventOfCode2021-12-25
Sea cucumber exercise

My (belated) solution to the Advent Of Code 2021 day 25.
The problem can be found here: https://adventofcode.com/2021/day/25.

Complexity analysis:
  complexity = 4*(E+S)*counter + n*m
  
  counter = number of needed iterations until the cucumbers stop
  number of unblocked east cucumbers = E
  number of unblocked south cucumbers = S
  n = height of grid
  m = width of grid
  
Explanation:
  n*m for initial search
  for each iteration:
    E*(4 checks: left, right at new location, up, and up at new location) + S*(4 checks)
