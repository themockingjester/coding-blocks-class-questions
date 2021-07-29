'''
                                                              Dynamic Programming


Reaching to the top of a staircase, it takes n steps.
The task can be accomplished either by climbing 1 step or 2 steps at a time.
In how many different ways can you climb to the top.
Note: n will be a positive integer.
Input Format

First line contains an integer n.
Constraints

None
Output Format

Print the total number of distinct ways you can climb to top.
Sample Input

2

Sample Output

2

Explanation

None

'''
n = int(input())

if n==0:
	print(1)
elif n==1:
	print(1)
else:
	dp=[0]*(n+1)
	dp[0]=1
	dp[1]=1

	for i in range(2,n+1):
		dp[i]=dp[i-1]+dp[i-2]

	print(dp[-1])
