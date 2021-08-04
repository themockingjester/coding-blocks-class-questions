'''
Kartik bhaiya gave monu an array 'nums' of n elements and an integer k .Find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k . monu is not good in maths help monu to solve the problem.
Return true if nums[i] = nums[j] and the absolute difference between i and j is at most k,otherwise return false.
Input Format

First line contains integer n as size of array.
Next N lines contains element of array.
Last line contains value of k.
Constraints

None
Output Format

The output will be of the boolean form (true/false).
Sample Input

4
1 
2 
3 
1
3

Sample Output

true

Explanation

None


'''
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
tar=int(input())
dic={}
for i in range(n):
    if arr[i] not in dic:
        dic[arr[i]]=i
    else:
        if i != dic[arr[i]] and abs(i-dic[arr[i]])<=tar:
            print('true')
            break
else:
    print('false')
