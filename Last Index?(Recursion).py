'''
                                                              Recursion based
                                                              


Take as input N, the size of array. Take N more inputs and store that in an array. Take as input M, a number. Write a recursive function which returns the last index at which M is found in the array and -1 if M is not found anywhere. Print the value returned.


Input Format
Enter a number N and add N more numbers to an array, then enter number M to be searched


Constraints
None


Output Format
Display the last index at which the number M is found


Sample Input
5
3
2
1
2
3
2


Sample Output
3
                                                                  
'''
class MyClass:
	def lastoccourance(self,arr,index,target):
		if index==-1:
			return -1
		if arr[index]==target:
			return index
		else:
			return self.lastoccourance(arr,index-1,target)
n=int(input())
arr=[]
for i in range(n):
	arr.append(int(input()))

target = int(input())
print(MyClass().lastoccourance(arr,len(arr)-1,target))
