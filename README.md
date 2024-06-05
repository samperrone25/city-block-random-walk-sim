This repostiory contains functions that can simulate Monte-Carlo style >=2 people random-walking in >=2 directions in a space of dimension >= 2.
The goal of these simulations were to test the theoretical result to the below question.

Question:
On an n street x n street, perfectly square, uniform city grid one person starts in the bottom left corner and another in the top right. They wish to meet after work.

given:
 - person 1 is random-walking with directions up and right, deciding their next move at each street intersection
 - person 2 is random walking with directions down and left
 - both start walking at the same time and with the same speed,

What is the probability that they meet?


My answer:
The probability that they meet = (total number of path pairs for the two people that result in a meet) / (total number of path pairs)

Given the grid is perfectly square it will take a person n moves until they arrive at a street intersection on the diagonal of the city grid that lies halfway between the two people. 
Furthermore if they haven't met at this time then they won't ever meet given the directions available to each person.
Therefore I will consider paths of length n for each player, where a path consists of 'H' and 'V' where H = horizontal move and V = vertical move.

The following path pairs meet (n=5):
('HVVVH', 'HVHHV')
('HHHHH', 'VVVVV')
('VVVVH', 'HHVHH')
While these dont:
('HHHHH', 'VVVVH')
('HVHVH', 'HVHHV')
and in general if person 1 has a path consisting of i H's and n-i V's then a meet will occur if person 2 has a path consisting of n-i H's and i V's

How many unique paths of length n can person 1 take with i H's and n-i V's?
n! arrangements, i duplicate H'S, n-i duplicate V's, so n! / (n-i)!i!

How many unique paths of length n can person 2 take with n-i H's and i V's? (to meet person 1)
n! arrangements, n-i duplicate H'S, i duplicate V's, so n! / i!(n-i)! which conveniently equals the previous expression and is also nCi (binomial coefficient)

How many unique path pairs can they both take?
number of strings with Alphabet = {H,V} and length = n will be 2^n, as we are considering pairs this will be squared to 2^(2n)

Final answer = Sum (0<=i<=n) (nCi)^2   /   2^(2n)


Monte Carlo simluations (took roughly 15sec):
100,000 simulations for n = 6, result:
![image](https://github.com/samperrone25/city-block-random-walk-sim/assets/68690083/8770b1b1-d7ff-447e-a49e-0a37810f0910)


100,000 simulations for n = 15, result:
![image](https://github.com/samperrone25/city-block-random-walk-sim/assets/68690083/fc9371a9-b33b-4230-907c-2309e848f273)
Where theoretical value is the value computed by the previous formula
