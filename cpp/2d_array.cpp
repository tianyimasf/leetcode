#include <string>
#include <iostream>
#include <vector>

using namespace std;

/*
 * Question specification: https://www.hackerrank.com/challenges/2d-array/problem
 *
 * This program is written in C++11.
 * 
 * Complete the 'hourglassSum' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */

int hourglassSum(vector<vector<int>> arr) {
    int max = -64; // lowest possible sum - 1
    for (int i = 0; i < 4; i++){ // iterate through each possible row number
        for (int j = 0; j < 4; j++){ // iterate through each possible column number
            int curr = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2];
            if (curr > max){
                max = curr;
            }
        }
    }
    return max;
}

/* Runtime analysis
 * 
 * 1. Set initial max value (# operation = 1)
 * 2. Calculate all 16 possible hourglass sum. For every sum, 
 * we add up 7 values and compare the sum to max (# operations = 8).
 * Suppose the matrix size is not fixed (n), then O(n) = 8(n-2), optimal.
 * 
*/