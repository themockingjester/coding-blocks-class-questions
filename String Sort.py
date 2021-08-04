'''


Nishant is a very naughty boy in Launchpad Batch. One day he was playing with strings, and randomly shuffled them all. Your task is to help Nishant Sort all the strings ( lexicographically ) but if a string is present completely as a prefix in another string, then string with longer length should come first. Eg bat, batman are 2 strings and the string bat is present as a prefix in Batman - then sorted order should have - Batman, bat.
Input Format

N(integer) followed by N strings.
Constraints

N<=1000
Output Format

N lines each containing one string.
Sample Input

3
bat
apple
batman

Sample Output

apple
batman
bat

Explanation

In mathematics, the lexicographic or lexicographical order (also known as lexical order, dictionary order, alphabetical order or lexicographic(al) product) is a generalization of the way words are alphabetically ordered based on the alphabetical order of their component letters.


'''
n=int(input())
arr=[]
for i in range(n):

	arr.append(input())
arr=sorted(arr)
for i in range(len(arr)):
	if i==len(arr)-1:
		pass
	else:
		if arr[i] not in arr[i+1]:
			pass
		else:
			if len(arr[i+1])>len(arr[i]):
				temp=arr[i]
				arr[i]=arr[i+1]
				arr[i+1]=temp
	print(arr[i])
