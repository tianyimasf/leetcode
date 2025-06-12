#include <string>
#include <iostream>
#include <vector>

using namespace std;

/*
 * Question specification: https://www.hackerrank.com/challenges/arrays-ds/problem
 *
 * This program is written in C++11.
 *
 * Complete the 'reverseArray' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts INTEGER_ARRAY a as parameter.
 */

vector<int> reverseArray(vector<int> a) {
    const int arr_len = a.size();
    if (arr_len == 0) { return {}; }
    vector<int> reversed_arr(arr_len);
    for (int i = 0; i < arr_len; i++) {
        reversed_arr[arr_len-i-1] = a[i];
    }
    return reversed_arr;
}

/* Runtime analysis
 * 
 * 1. Get array length = 1 operation
 * 2. Loop through original array a and fill reversely the new, 
 * empty array of equal length: O(n) where n = array length.
 * 
 * Conclusion: runtime = O(n) which is optimal in this case.
 * 
*/