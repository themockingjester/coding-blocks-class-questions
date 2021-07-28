'''
                                                    Recursion and Dynamic Programming


Given a gold mine (M) of n*m dimensions. Each field in this mine contains a positive integer which is the amount of gold in tons. Initially the miner is at first column but can be at any row. He can move only (right->,right up /,right down) that is from a given cell, the miner can move to the cell diagonally up towards the right or right or diagonally down towards the right. Your task is to find out maximum amount of gold which he can collect.
Input Format

The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains an integer n and m denoting the size of the matrix. Then in the next line are n*m space separated values of the matrix.
Constraints

1<=T<=100

1<=n,m<=20

1<=M[][]<=100
Output Format

For each test case in a new line print an integer denoting the max gold the miner could collect.
Sample Input

2
3 3 
1 3 3 2 1 4 0 6 4
2 2
1 2 3 4

Sample Output

12
7

                                                   
'''

class Solution:
    def solve(self,cc,cr,n,m,M):
        if cc>=m or cr>=n or 0>cc or 0>cr:
            return 0
        if self.mat[cr][cc]!=-1:
            return self.mat[cr][cc]
        self.mat[cr][cc]=max(self.solve(cc-1,cr,n,m,M),self.solve(cc-1,cr-1,n,m,M),self.solve(cc-1,cr+1,n,m,M))+M[cr][cc]
        
        self.solve(cc,cr+1,n,m,M)
        self.solve(cc+1,cr,n,m,M)
        return self.mat[cr][cc]
    def maxGold(self, n, m, M):
        self.mat=[[-1 for i in range(len(M[0]))] for j in range(len(M))]
        
        self.solve(0,0,n,m,M)
        maxi=self.mat[0][-1]
        maxi=self.mat[0][-1]
        for i in range(len(self.mat)):
            if self.mat[i][-1]>maxi:
                maxi=self.mat[i][-1]
        return maxi
t=int(input())
for i in range(t):
	temp=input().split(" ")
	n,m=int(temp[0]),int(temp[1])
	temp=input().split(" ")
	M = [int(j) for j in temp if len(j)>0]
	ans=[]
	ctr=0
	for j in range(n):
		lis=[]
		for p in range(m):
			lis.append(M[ctr])
			ctr+=1
		ans.append(lis.copy())
	M=ans.copy()
	
	
	
	print(Solution().maxGold(n,m,M))
