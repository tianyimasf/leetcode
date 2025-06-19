#include <string>
#include <iostream>
#include <vector>
using std::vector;

/*
 * Complete the 'dynamicArray' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. 2D_INTEGER_ARRAY queries
 */
 
// Expand arr[idx] by doubling the size allocated.
void helper_extendArrIdx(int** arr, int idx){
    int newSize = sizeof(arr[idx])*2;
    if (newSize > pow(10, 5)) {newSize = pow(10, 5);} // cap the size
    int* newArrIdx = new int[newSize];
    for (int i = 0; i < newSize/2; i++){
        newArrIdx[i] = arr[idx][i];
    }
    delete[] arr[idx];
    arr[idx] = newArrIdx;
}

// Expand answers by doubling the size allocated.
void helper_extendAnswers(int* answers){
    int newSize = sizeof(answers)*2;
    if (newSize > pow(10, 5)) {newSize = pow(10, 5);} // cap the size
    int* newAnswers = new int[newSize];
    for (int i = 0; i < newSize/2; i++){
        newAnswers[i] = answers[i];
    }
    delete[] answers;
    answers = newAnswers;
}

// Perform query 1 x y
void helper_query1(int x, int y, int** arr, int* lastIdx, int lastAnswer){
    int idx = lastAnswer ^ x;
    int lastIdxCurr = lastIdx[idx];
    if (sizeof(arr[idx]) - 1 == lastIdxCurr){
        helper_extendArrIdx(arr, idx);
    }
    arr[idx][lastIdxCurr + 1] = y; lastIdx[idx]++;
}

// Perform query 2 x y
void helper_query2(int x, int y, int** arr, int lastAnswer, int* answers, int lastAnswerIdx){
    int idx = lastAnswer ^ x;
    lastAnswer = arr[idx][y % sizeof(arr[idx])];
    if (sizeof(answers) - 1 == lastAnswerIdx){
        helper_extendAnswers(answers);
    }
    answers[lastAnswerIdx + 1] = lastAnswer; lastAnswerIdx++; 
}

vector<int> helper_dynamicArr2vector(int* answers, int lastAnswerIdx){
    vector<int> answers_v(lastAnswerIdx + 1);
    for (int i = 1; i <= lastAnswerIdx; i++) {
        answers_v[i] = answers[i];
    }
    return answers_v;
}

vector<int> dynamicArray(int n, vector<vector<int>> queries) {
    int initialSize = static_cast<int>(log2(sizeof(queries)));
    // Initialize arr
    int** arr = new int*[n];
    for (int i = 0; i < n; ++i) {
        arr[i] = new int[initialSize];
    }
    // Initialize lastIdx to track the last element's index for each array
    int* lastIdx = new int[n];
    for (int i = 0; i < n; ++i) {
        lastIdx[i] = -1;
    }
    int lastAnswer = 0;
    // Initialize answers to store all answers
    int* answers = new int[initialSize];
    for (int i = 0; i < initialSize; ++i){
        answers = 0;
    }
    int lastAnswerIdx = 0;
    // Perform all queries
    for (int i = 0; i < sizeof(queries); i++){
        vector<int> query = queries[i];
        if (query[0] == 1) {helper_query1(query[1], query[2], arr, lastIdx, lastAnswer);}
        else if (query[0] == 2) {helper_query2(query[1], query[2], arr, lastAnswer, answers, lastAnswerIdx);}
    }
    vector<int> answers_v = helper_dynamicArr2vector(answers, lastAnswerIdx);
    return answers_v;
}
