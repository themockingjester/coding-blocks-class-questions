'''
                                                        Recursion based


Take as input N, a number. Write a recursive function which prints counting from 0 to N in lexicographical order. In lexicographical (dictionary) order 10, 100 and 109 will be printed before 11.


Input Format
Enter a number N.


Constraints
None


Output Format
Display all the numbers upto N in a lexicographical order


Sample Input
10

Sample Output
0 1 10 2 3 4 5 6 7 8 9 


'''
class MyClass:
	def solve(self,n,sums):
		if sums>n:
			return 0
		print(sums,end=" ")
		if sums==0:
			for i in range(1,10):
				
				self.solve(n,10*sums+i)
		else:
			for i in range(10):
				
				self.solve(n,10*sums+i)
n = int(input())
MyClass().solve(n,0)
