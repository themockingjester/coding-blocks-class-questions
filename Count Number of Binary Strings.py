'''
                                                                Dynamic Programmig and Fibonacci Series based


You are provided an integers N. You need to count all possible distinct binary strings of length N such that there are no consecutive 1’s.
Input Format

First line contains integer t which is number of test case. For each test case, it contains an integer n which is the the length of Binary String.
Constraints

1<=t<=100 1<=n<=90
Output Format

Print the number of all possible binary strings.
Sample Input

2
2
3

Sample Output

3
5

Explanation

1st test case : 00, 01, 10 2nd test case : 000, 001, 010, 100, 101

'''



t=int(input())
for i in range(t):
	n=int(input())
	dp=[0]*(n+1)
	if n==0:
		print(0)
	elif n==1:
		print(2)
	else:
		dp[1],dp[2]=2,3
		for i in range(3,n+1):
			dp[i]=dp[i-1]+dp[i-2]
		print(dp[-1])
