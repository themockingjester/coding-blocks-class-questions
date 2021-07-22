'''
                                                                  Recursion based
                                                                  


Take as input N, the size of array. Take N more inputs and store that in an array. Take as input M, a number. Write a recursive function which returns the first index at which M is found in the array and -1 if M is not found anywhere. Print the value returned.


Input Format
Enter a number N and add N more elements to an array, then enter a number M


Constraints
None


Output Format
Display the first index at which number M is found


Sample Input
5
3
2
1
2
2
2



Sample Output
1


'''
class First:
	def firstOccurance(self,ctr,n,arr,target):
		if ctr==n:
			return -1
		if arr[ctr]==target:
			return ctr
		else:
			return self.firstOccurance(ctr+1,n,arr,target)
n = int(input())
arr=[]

for i in range(n):
	arr.append(int(input()))

target = int(input())
print(First().firstOccurance(0,n,arr,target))
