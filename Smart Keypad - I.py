'''
                                                             Recursion based
                                                             


You will be given a numeric string S. Print all the possible codes for S.

Following vector contains the codes corresponding to the digits mapped.

string table[] = { " ", ".+@$", "abc", "def", "ghi", "jkl" , "mno", "pqrs" , "tuv", "wxyz" };

For example, string corresponding to 0 is " " and 1 is ".+@$"

Input Format
A single string containing numbers only.

Constraints
length of string <= 10

Output Format
All possible codes one per line in the following order.

    The letter that appears first in the code should come first


Sample Input
12

Sample Output

.a
.b
.c
+a
+b
+c
@a
@b
@c
$a
$b
$c


Explanation
For code 1 the corresponding string is .+@$ and abc corresponds to code 2.

'''

class MyClass:
	def __init__(self):
		self.dic = {'0':" ",'1':".+@$", '2':"abc", '3':"def", '4':"ghi", '5':"jkl" , '6':"mno", '7':"pqrs" , '8':"tuv", '9':"wxyz"}
	def solve(self,n,ans,curr):
		if curr==len(n):
			print(ans)
			return
		for i in self.dic[n[curr]]:
			self.solve(n,ans+i,curr+1)

MyClass().solve(input(),"",0)
