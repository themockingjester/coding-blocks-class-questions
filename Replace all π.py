'''
                                                                        Recursion based


Replace all occurrences of pi with 3.14

Input Format
Integer N, no of lines with one string per line


Constraints
0 < N < 1000
0 <= len(str) < 1000


Output Format
Output result one per line


Sample Input
3
xpix
xabpixx3.15x
xpipippixx



Sample Output
x3.14x
xab3.14xx3.15x
x3.143.14p3.14xx


Explanation
All occurrences of pi have been replaced with "3.14".

'''
class MyClass:
	def __init__(self):
		self.dic={}
	def replacer(self,s,index,ans):
		if len(s)<2:
			return s
		if index+1 <len(s):
			if s[index:index+2]=="pi" and index not in self.dic and index+1 not in self.dic:
				self.dic[index]=1
				self.dic[index+1]=1
				ans+='3.14'
			else:
				if index not in self.dic:
					ans+=str(s[index])
			return self.replacer(s,index+1,ans)
		else:
			if index not in self.dic:
				ans+=s[index]
			return ans
				
n = int(input())
for i in range(n):
	s=input()
	print(MyClass().replacer(s,0,""))

		



