<p align="center">
  <img alt="Foobar Icon" src="https://github.com/user-attachments/assets/e376dcf7-d98d-4a3d-af39-1109e437adaf" width="70" />
</p>
<div align="center">
  <img alt="Python Badge" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
</div>
<h1 align="center">
  GoogleFoobarChallenge
</h1>

Solutions submitted for the Google Foobar Challenge

#### Challenge 1

[Challenge 1 was not saved]

#### Challenge 2
<pre>
Create a function solution to calculate the minimum number "Chess Knights Moves" 
needed to get from any position x on the grid to any other position y, given x 
(starting position) and y (ending position)
---------------------------
|  0  1  2  3  4  5  6  7 |
|  8  9 10 11 12 13 14 15 |
| 16 17 18 19 20 21 22 23 |
| 24 25 26 27 28 29 30 31 |
| 32 33 34 35 36 37 38 39 |
| 40 41 42 43 44 45 46 47 |
| 48 49 50 51 52 53 54 55 |
| 56 57 58 59 60 61 62 63 |
---------------------------

Example Cases
==========
Ex 1:
Input: solution.solution(0, 10)
Output: 1

Ex 2:
Input: solution.solution(35, 37)
Output: 2
</pre>

#### Challenge 3

<pre>
| 7
| 4 8
| 2 5 9
| 1 3 6 10

Each cell can be represented as points (x, y), with x being the distance from the vertical wall, 
and y being the height from the ground. 

For example, the bunny worker at (1, 1) has ID 1, the bunny worker at (3, 2) has ID 9, 
and the bunny worker at (2,3) has ID 8. This pattern of numbering continues indefinitely 

Write a function solution(x, y) which returns the worker ID of the bunny at location (x, y). 
Each value of x and y will be at least 1 and no greater than 100,000. Since the worker ID 
can be very large, return your solution as a string representation of the number.

Example Cases
==========
Ex 1
Input: solution.solution(5, 10)
Output: 96

Ex 2
Input: solution.solution(3, 2)
Output: 9
</pre>

#### Challenge 4

<pre>
There are two types: Mach bombs (M) and Facula bombs (F).
Bombs self-replicate via one of two distinct processes: 
Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created;
Every Facula bomb spontaneously creates a Mach bomb.

You need to know how many replication cycles (generations) it will take to generate 
the correct amount of bombs.

Write a function solution(M, F);
where M and F are the number of Mach and Facula bombs needed. Return the fewest number 
of generations (as a string) that need to pass before you'll have the exact number of 
bombs necessary, or the string "impossible" if this can't be done! 

Example Cases
==========

Ex 1
Input: solution.solution('4', '7')
Output: 4

Ex 2
Input: solution.solution('2', '1')
Output: 1
</pre>
