'''
                                                            Recursion based
                                                            


Take as input N, a number. Take N more inputs and store that in an array. Write a recursive function which reverses the array. Print the values of reversed array.


Input Format
Enter a number N and take N more inputs


Constraints
None


Output Format
Display values of the reversed array



Sample Input
4
1
2
3
4



Sample Output
4 3 2 1

'''


class Reverse:
	def __init__(self):
		self.new=[]
		
	def rev(self,arr,ctr):
		if -1*ctr<=len(arr):
			self.new.append(arr[ctr])
			ctr-=1
			self.rev(arr,ctr)

n=int(input())
arr=[]
for i in range(n):
	arr.append(int(input()))
	
obj=Reverse()
obj.rev(arr,-1)
for i in obj.new:
	print(i,end=" ")
