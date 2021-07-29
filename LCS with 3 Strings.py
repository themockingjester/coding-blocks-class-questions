'''
                                                    Dynamic Programming



Given 3 strings ,the task is to find the longest common sub-sequence in all three given sequences.
Input Format

First line contains first string . Second line contains second string. Third line contains the third string.
Constraints

The length of all strings is |s|< 200
Output Format

Output an integer denoting the length of longest common subsequence of above three strings.
Sample Input

GHQWNV
SJNSDGH
CPGMAH

Sample Output

2

Explanation

"GH" is the longest common subsequence

'''

A=input()
B=input()
C=input()
dp=[[[0 for i in range(len(A)+1)] for j in range(len(B)+1)] for k in range(len(C)+1)]
for k in range(1,len(C)+1):
	for j in range(1,len(B)+1):
		for i in range(1,len(A)+1):
			if C[k-1]==B[j-1] and C[k-1]==A[i-1]:
				dp[k][j][i]=dp[k-1][j-1][i-1]+1
			else:
				dp[k][j][i]=max(dp[k-1][j][i],dp[k][j-1][i],dp[k][j][i-1])
print(dp[-1][-1][-1])
