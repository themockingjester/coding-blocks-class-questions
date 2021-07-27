'''
                                                    Fibonacci and Dynamic Programming


Given N, count the number of ways to express N as sum of 1, 3 and 4.
Input Format

First line contains the size of the array. Next line contains array elements.
Constraints

1 <= N <= 108
Output Format

Print the integer answer.
Sample Input

4

Sample Output

4 

Explanation

1+1+1+1
1+3
3+1
4


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
		sums=0
		for j in [1,3,4]:
			if i-j<0:
				pass
			else:
				sums+=dp[i-j]
		dp[i]=sums

	print(dp[-1])
