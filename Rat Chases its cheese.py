'''
                                                            Recursion and BackTracking based
                                                            


You are given an N*M grid. Each cell (i,j) in the grid is either blocked, or empty. The rat can move from a position towards left, right, up or down on the grid.
Initially rat is on the position (1,1). It wants to reach position (N,M) where it's cheese is waiting for. There exits a unique path in the grid . Find that path and help the rat reach its cheese.


Input Format
First line contains 2 integers N and M denoting the rows and columns in the grid.
Next N line contains M characters each. An 'X' in position (i,j) denotes that the cell is blocked and ans 'O' denotes that the cell is empty.


Constraints
1 <= N , M <= 10


Output Format
Print N lines, containing M integers each. A 1 at a position (i,j) denotes that the (i,j)th cell is covered in the path and a 0 denotes that the cell is not covered in the path.
If a path does not exits then print "NO PATH FOUND"



Sample Input
5 4
OXOO
OOOX
XOXO
XOOX
XXOO


Sample Output
1 0 0 0 
1 1 0 0 
0 1 0 0 
0 1 1 0 
0 0 1 1 


'''
class MyClass:
	def __init__(self):
		self.flag = False
		
	def solve(self,mat,given,cr,cc,c,r):
		if cr==r-1 and cc==c-1:
			mat[-1][-1]=1
			for i in range(r):
				for j in range(c):
					print(mat[i][j],end=" ")
				print()
			self.flag=True
			return
		if cr<0 or cr==r or cc<0 or cc==c:
			return
		if given[cr][cc]=='X' or mat[cr][cc]==1:
			return
		mat[cr][cc]=1
		self.solve(mat,given,cr+1,cc,c,r)
		self.solve(mat,given,cr,cc+1,c,r)
		self.solve(mat,given,cr-1,cc,c,r)
		self.solve(mat,given,cr,cc-1,c,r)
		mat[cr][cc]=0
s=input()
s =s.split(" ")
r=int(s[0])
c=int(s[1])
arr=[]
for i in range(r):
	temp=[]
	s=input()
	

	for j in range(c):
		temp.append(s[j])
	arr.append(temp)
mat = [[0 for i in range(c)] for j in range(r)]
o=MyClass()
o.solve(mat,arr,0,0,c,r)
if o.flag==False:
	print("NO PATH FOUND")

	

