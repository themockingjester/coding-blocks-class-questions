'''
                                                              Recursion based

Take as input str, a string. Write a recursive function which returns a new string in which all duplicate consecutive characters are separated by a ‘ * ’. E.g. for “hello” return “hel*lo”. Print the value returned


Input Format
Enter a String


Constraints
1<= Length of string <= 10^4


Output Format
Display the resulting string (i.e after inserting (*) b/w all the duplicate characters)


Sample Input
hello


Sample Output
hel*lo


Explanation
We insert a "*" between the two consecutive 'l' .

'''

class MyClass:
	def formatting(self,s,ans,index,n):
		if index+1==n:
			ans+=s[index]
			return ans
		if s[index]==s[index+1]:
			ans+=s[index]+"*"
			return self.formatting(s,ans,index+1,n)
		else:
			ans+=s[index]
			return self.formatting(s,ans,index+1,n)
		
s = input()
print(MyClass().formatting(s,"",0,len(s)))
