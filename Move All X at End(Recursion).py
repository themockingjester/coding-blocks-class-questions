'''
                                                                Recursion based
                                                                


Take as input str, a string. Write a recursive function which moves all ‘x’ from the string to its end.
E.g. for “abexexdexed” return “abeedeedxxx”.
Print the value returned


Input Forma
Single line input containing a string


Constraints
Length of string <= 1000


Output Format
Single line displaying the string with all x's moved at the end


Sample Input
axbxc


Sample Output
abcxx


Explanation
All x's are moved to the end of string while the order of remaining characters remain the same.

'''
class MyClass:
	def __init__(self):
		self.count=0
	def MoveX(self,s,index,ans):
		if index==len(s):
			return ans
		if s[index]=='x':
			pass
			self.count+=1
		else:
			ans+=s[index]
		return self.MoveX(s,index+1,ans)
s = input()
o = MyClass()
new = o.MoveX(s,0,"")

for i in range(o.count):
	new+='x'
print(new)
