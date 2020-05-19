// #------------------------------------------QUESTION 1------------------------------------------------------------------------------------------------
// # An array is a type of data structure that stores elements of the same type in a contiguous block of memory. In an array, A, of size N, each memory
// # location has some unique index, i (where 0<=i<N), that can be referenced as  A[i].
// #
// # Given an array,A , of  N integers, print each element in reverse order as a single line of space-separated integers.
// #
// # Note: If you've already solved our C++ domain's Arrays Introduction challenge, you may want to skip this.
// #
// # Input Format
// #
// # The first line contains an integer, N (the number of integers in A ).
// # The second line contains N space-separated integers describing A.
// #
// # Output Format
// #
// # Print all N integers in  A in reverse order as a single line of space-separated integers.

//-------------------------------------------SOLUTION------------------------------------------------------------------------------------------------



// #---------------------------------------QUESTION 2--------------------------------------------------------------
// # Given a binary array, find the maximum number of consecutive 1s in this array.
// #
// # Example 1:
// # Input: [1,1,0,1,1,1]
// # Output: 3
// # Explanation: The first two digits or the last three digits are consecutive 1s.
// #     The maximum number of consecutive 1s is 3.
// # Note:
// #
// # The input array will only contain 0 and 1.
// # The length of input array is a positive integer and will not exceed 10,000

//--------------------------------------------SOLUTION--------------------------------------------------------------------------------------------
public int findMaxConsecutiveOnes(int[] nums) {
        int counter = 0;
        int maxConcecutive = 0;
        for(int i=0;i<nums.length;i++)
            if(nums[i] == 1){
                counter++;
                maxConcecutive = Math.max(counter, maxConcecutive);
            }else{
                counter = 0;
            }
        return maxConcecutive;
    }

// #----------------------------------------QUESTION 3-----------------------------------------------------------
// # Given an array nums of integers, return how many of them contain an even number of digits.
// #
// #
// # Example 1:
// #
// # Input: nums = [12,345,2,6,7896]
// # Output: 2
// # Explanation:
// # 12 contains 2 digits (even number of digits).
// # 345 contains 3 digits (odd number of digits).
// # 2 contains 1 digit (odd number of digits).
// # 6 contains 1 digit (odd number of digits).
// # 7896 contains 4 digits (even number of digits).
// # Therefore only 12 and 7896 contain an even number of digits.

//---------------------------------------------SOLUTION-----------------------------------------------------------
public int findNumbers(int[] nums) {
        int count = 0;

        for (int num: nums){
            if (String.valueOf(num).length() % 2 == 0){
                count++;
            }
        }
        return count;

    }
// #----------------------------------------QUESTION 4------------------------------------------------------------
// # Given a  6 by 6 ,2D Array,arr :
// #
// # 1 1 1 0 0 0
// # 0 1 0 0 0 0
// # 1 1 1 0 0 0
// # 0 0 0 0 0 0
// # 0 0 0 0 0 0
// # 0 0 0 0 0 0
// #
// # We define an hourglass in A to be a subset of values with indices falling in this pattern in arr's graphical representation:
// #
// # a b c
// #   d
// # e f g
// #
// # There are 16 hourglasses in arr, and an hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum.
// #
// # For example, given the 2D array:
// #
// # -9 -9 -9  1 1 1
// #  0 -9  0  4 3 2
// # -9 -9 -9  1 2 3
// #  0  0  8  6 6 0
// #  0  0  0 -2 0 0
// #  0  0  1  2 4 0
// #
// #  We calculate the following  16 hourglass values:
// #
// #  -63, -34, -9, 12,
// # -10, 0, 28, 23,
// # -27, -11, -2, 10,
// # 9, 17, 25, 18
// #
// # Our highest hourglass value is 28 from the hourglass:
// #
// # 0 4 3
// #   1
// # 8 6 6

//---------------------------------------------------SOLUTION------------------------------------------------------------

static int hourglassSum(int[][] arr) {
        int rows = arr.length;
        int columns = arr[0].length;
        int maxSum = Integer.MIN_VALUE;

        for(int i=0;i<rows-2;i++){
            for(int j=0;j<columns-2;j++){
                int current_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j]+ arr[i+2][j+1] + arr[i+2][j+2];
                maxSum = Math.max(maxSum, current_sum);
            }
        }

        return maxSum;

    }
