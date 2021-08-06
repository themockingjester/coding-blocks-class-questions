'''


Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars.
Input Format

First line contains a single integer N, denoting the number of bars in th histogram.
Next line contains N integers, ith of which, denotes the height of ith bar in the histogram.
Constraints

1<=N<=10^6
Height of each bar in histogram <= 10^9
Output Format

Output a single integer denoting the area of the required rectangle.
Sample Input

5
1 2 3 4 5

Sample Output

9

Explanation

The largest rectangle can be obtained of breadth=3 and length=3. Its starting index is 2 and ending index is 4 and it has a height of 3. Hence area = 3*3 = 9


'''
n=int(input())
arr=[int(i) for i in input().split(" ") if len(i)>0]
leftStack=[]
leftIndices=[]
for i in range(len(arr)):
	if len(leftStack)==0:
		leftStack.append(i)
		leftIndices.append(0)
	else:
		if arr[leftStack[-1]]<=arr[i]:
			
			leftIndices.append(leftStack[-1]+1)
			leftStack.append(i)
		else:
			while len(leftStack)!=0 and arr[leftStack[-1]]>arr[i]:
				leftStack.pop()
			if len(leftStack)==0:
				leftIndices.append(0)
			else:
				leftIndices.append(leftStack[-1]+1)
			leftStack.append(i)
rightStack=[]
rightIndices=[]
for i in range(len(arr)-1,-1,-1):
	if len(rightStack)==0:
		rightStack.append(i)
		rightIndices.append(len(arr)-1)
	else:
		if arr[rightStack[-1]]<=arr[i]:
			
			rightIndices.append(rightStack[-1]-1)
			rightStack.append(i)
		else:
			while len(rightStack)!=0 and arr[rightStack[-1]]>arr[i]:
				rightStack.pop()
			if len(rightStack)==0:
				rightIndices.append(len(arr)-1)
			else:
				rightIndices.append(rightStack[-1]-1)
			rightStack.append(i)
rightIndices=rightIndices[::-1]
maxi=0
for i in range(len(arr)):
	area=(rightIndices[i]-leftIndices[i]+1)*arr[i]
	if area>maxi:
		maxi=area
print(maxi)


