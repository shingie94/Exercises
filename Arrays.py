#------------------------------------------QUESTION 1------------------------------------------------------------------------------------------------
# An array is a type of data structure that stores elements of the same type in a contiguous block of memory. In an array, A, of size N, each memory
# location has some unique index, i (where 0<=i<N), that can be referenced as  A[i].
#
# Given an array,A , of  N integers, print each element in reverse order as a single line of space-separated integers.
#
# Note: If you've already solved our C++ domain's Arrays Introduction challenge, you may want to skip this.
#
# Input Format
#
# The first line contains an integer, N (the number of integers in A ).
# The second line contains N space-separated integers describing A.
#
# Output Format
#
# Print all N integers in  A in reverse order as a single line of space-separated integers.

#---------------------------------------SOLUTION---------------------------------------------------------------
def reverseArray(a):
    reverse = a[::-1]
    return reverse



#---------------------------------------QUESTION 2--------------------------------------------------------------
# Given a binary array, find the maximum number of consecutive 1s in this array.
#
# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
# Note:
#
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000

#----------------------------------------SOLUTION--------------------------------------------------------------
def findMaxConsecutiveOnes(self, nums):
        count = 0
        maxValue = 0

        for n in nums:
            if n == 1:
                count += 1
                maxValue = max(count, maxValue)
            else:
                count = 0

        return maxValue

#----------------------------------------QUESTION 3-----------------------------------------------------------
# Given an array nums of integers, return how many of them contain an even number of digits.
#
#
# Example 1:
#
# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation:
# 12 contains 2 digits (even number of digits).
# 345 contains 3 digits (odd number of digits).
# 2 contains 1 digit (odd number of digits).
# 6 contains 1 digit (odd number of digits).
# 7896 contains 4 digits (even number of digits).
# Therefore only 12 and 7896 contain an even number of digits.

#-----------------------------------------SOLUTION------------------------------------------------------------
def findNumbers(self, nums):
        count = 0
        for num in nums:
            if len(str(num))%2 == 0:
                count+=1
        return count
