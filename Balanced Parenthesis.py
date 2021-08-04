'''


You are given a string of brackets i.e. '{', '}' , '(' , ')', '[' , ']' . You have to check whether the sequence of parenthesis is balanced or not.
For example, "(())", "(())()" are balanced and "())(", "(()))" are not.
Input Format

A string of '(' , ')' , '{' , '}' and '[' , ']' .
Constraints

1<=|S|<=10^5
Output Format

Print "Yes" if the brackets are balanced and "No" if not balanced.
Sample Input

(())

Sample Output

Yes

Explanation

(()) is a balanced string.


'''
s=input()
arr=[]
dic={
	')':'(',
	'}':'{',
	']':'[',
}
for i in s:
	if i==')' and len(arr)!=0 and arr[-1]==dic[')']:
		arr.pop()
	else:
		arr.append(i)
if len(arr)==0:
	print('Yes')
else:
	print('No')
