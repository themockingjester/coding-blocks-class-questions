'''
                                                          Dynamic Programming


Given n friends, each one can remain single or can be paired up with some other friend. Each friend can be paired only once. Find out the total number of ways in which friends can remain single or can be paired up.
Input Format

First line contains an integer t denoting the number of test cases. Next t lines contain an integer n each.
Constraints

1<= n < 30
Output Format

Output t lines each line describing the answer.
Sample Input

1
3

Sample Output

4

Explanation

{1}, {2}, {3} : all single {1}, {2,3} : 2 and 3 paired but 1 is single. {1,2}, {3} : 1 and 2 are paired but 3 is single. {1,3}, {2} : 1 and 3 are paired but 2 is single. Note that {1,2} and {2,1} are considered same.

'''
t=int(input().split()[0])
for j in range(t):
	n=int(input().split()[0])
	if n==1:
		print(1)
		continue
	dp=[0]*(n)
	dp[0],dp[1]=1,2
	for i in range(2,len(dp)):
		dp[i]=dp[i-1]+(i)*dp[i-2]
	print(dp[-1])
