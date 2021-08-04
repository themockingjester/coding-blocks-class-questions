'''



Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
Input Format

First line contains integer N (size of the array) followed by N more integers.
Constraints

Output Format

Majority Element of array
Sample Input

3
1 1 2

Sample Output

1

Explanation

Number of 1's in the array is more than 3/2 , Hence majority element is 1

'''
n=int(input())
temp=input().split(" ")
arr=[int(i) for i in temp if len(i)>0]
dic={}
el=0
maxi=0
for i in range(n):
	if arr[i] not in dic:
		dic[arr[i]]=1
	else:
		dic[arr[i]]+=1
	if dic[arr[i]]>maxi:
		maxi=dic[arr[i]]
		el=arr[i]

print(el)


