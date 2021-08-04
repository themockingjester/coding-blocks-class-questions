'''
Given an array of n elements, check if the array contains any duplicates.
The function should return true if there are duplicates,otherwise return false.
Input Format

First line contains integer n as size of array.
Next line contains a n integer as element of array.
Constraints

None
Output Format

The output will be of the boolean form.
Sample Input

4
1 2 3 1

Sample Output

true

Explanation

None

'''
n=int(input())
temp=input().split(" ")
arr=[int(i) for i in temp if len(i)>0]
dic={}
for i in range(n):
	if arr[i] not in dic:
		dic[arr[i]]=1
	else:
		print("true")
		break
else:
	print("false")
	
