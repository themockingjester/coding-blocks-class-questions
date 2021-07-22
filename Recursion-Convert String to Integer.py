'''
                                                                  Recursion based
                                                                  


Take as input str, a number in form of a string. Write a recursive function to convert the number in string form to number in integer form. E.g. for “1234” return 1234. Print the value returned.


Input Format
Enter a number in form of a String


Constraints
1 <= Length of String <= 10


Output Format
Print the number after converting it into integer


Sample Input
1234


Sample Output
1234


Explanation
Convert the string to int. Do not use any inbuilt functions.

'''
class MyClass:

	def convert(self,ans,s,n,index):
		if index==n:
			return ans
		ans=ans*10+int(s[index])
		return self.convert(ans,s,n,index+1)
s = input()
print(MyClass().convert(0,s,len(s),0))
