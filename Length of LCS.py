'''
                                                                  Dynamic Programming


A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. For example, the sequence {A,B,D} is a subsequence of {A,B,C,D,E,F}, obtained after removal of elements C, E and F.

Given two strings A and B of size n and m respectively, you have to find the length of Longest Common Subsequence(LCS) of strings A and B, where LCS is the longest sequence present in both A and B.
Input Format

Two strings A and B.
Constraints

1 <= n,m <= 10^3
Output Format

Output the LCS of A and B.
Sample Input

abc
acd

Sample Output

2


'''
s1=input()
s2=input()
dp=[[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
for i in range(1,len(s1)+1):
	for j in range(1,len(s2)+1):
		if s2[j-1]==s1[i-1]:
			dp[i][j]=dp[i-1][j-1]+1
		else:
			dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[-1][-1])
