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

#----------------------------------------QUESTION 4------------------------------------------------------------
# Given a  6 by 6 ,2D Array,arr :
#
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
#
# We define an hourglass in A to be a subset of values with indices falling in this pattern in arr's graphical representation:
#
# a b c
#   d
# e f g
#
# There are 16 hourglasses in arr, and an hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum.
#
# For example, given the 2D array:
#
# -9 -9 -9  1 1 1
#  0 -9  0  4 3 2
# -9 -9 -9  1 2 3
#  0  0  8  6 6 0
#  0  0  0 -2 0 0
#  0  0  1  2 4 0
#
#  We calculate the following  16 hourglass values:
#
#  -63, -34, -9, 12,
# -10, 0, 28, 23,
# -27, -11, -2, 10,
# 9, 17, 25, 18
#
# Our highest hourglass value is 28 from the hourglass:
#
# 0 4 3
#   1
# 8 6 6

#---------------------------------------------------SOLUTION-----------------------------------------------------------------
def hourglassSum(arr):
    sum = 0
    max_sum = -63

    for i in range(0,len(arr)-2):
        for j in range(0,len(arr[0])-2):
            sum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            max_sum = max(sum,max_sum)

    return(max_sum)
# //-------------------------------------------------QUESTION 5----------------------------------------------------------
# // You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates.
# // You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order.
# //
# // For example, given the array arr = [7, 1, 3, 2, 4, 5, 6] we perform the following steps:
# //
# // i   arr                         swap (indices)
# // 0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
# // 1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
# // 2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
# // 3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
# // 4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
# // 5   [1, 2, 3, 4, 5, 6, 7]
# //
# // It took 5 swaps to sort the array.
# //------------------------------------------------SOLUTION-------------------------------------------------------------
def minimumSwaps(arr):
    swaps = 0
    n = len(arr)
    for i in range(0,n):
        while arr[i] != i+1:
            temp = arr[i]
            arr[i] = arr[temp-1]
            arr[temp-1] = temp
            swaps+=1

    return swaps

# ---------------------------------------------------QUESTION 6------------------------------------------------------------
# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#
# Example 1:
#
# Given nums = [3,2,2,3], val = 3,
#
# Your function should return length = 2, with the first two elements of nums being 2.
#
# It doesn't matter what you leave beyond the returned length.

#---------------------------------------------------SOLUTION----------------------------------------------------------------
 def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                # reduce array size by one
                n-=1
            else:
                i+=1

        return n
# --------------------------------------------------QUESTION 7---------------------------------------------------------------
# Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography. During his last hike he took exactly n steps.
# For every step he took, he noted if it was an uphill, U , or a downhill, D step. Gary's hikes start and end at sea level and each step up or down represents a 1 unit change in altitude.
# We define the following terms:
#
# A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
# A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
# Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.
#
# For example, if Gary's path is s=[DDUUUUDD] , he first enters a valley 2 units deep. Then he climbs out an up onto a mountain 2 units high.
# Finally, he returns to sea level and ends his hike.
#-------------------------------------------------SOLUTION------------------------------------------------------------------
def countingValleys(n, s):
    valley = 0
    sealevel = 0

    for steps in s:
        if steps == 'U':
            sealevel+=1
            if sealevel == 0:
                valley+=1
        else:
            sealevel-=1
    return valley
