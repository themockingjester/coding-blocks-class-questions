'''
                                                        Dynamic Programming



A professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping him from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money he can rob tonight without alerting the police.
Input Format

First line contains integer t as number of testcases. Second line contains integer n as size of array. Third line contains a single integer as element of array.
Constraints

None
Output Format

Print the maximum money as output.
Sample Input

1
4
1 2 3 1

Sample Output

4


'''


t=int(input().split(" ")[0])
for i in range(t):
	n=int(input().split(" ")[0])
	temp=input().split(" ")
	nums=[int(i) for i in temp if len(i)>0]
	previous=0
	dp=nums.copy()
	for i in range(len(nums)):
		
		previous=i
		for j in range(i,len(nums)):
			
			if j==i:
				
				continue
			elif j>=previous+2:
				t1=dp[previous]
				t2=dp[j]
				if t2>=t1+nums[j]:
					continue
				else:

					dp[j]=t1+nums[j]
					#previous=j

	print(max(dp))
