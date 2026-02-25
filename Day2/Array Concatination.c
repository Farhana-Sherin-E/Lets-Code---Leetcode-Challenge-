/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getConcatenation(int* nums, int n, int* newSize) {
    int *ans = (int*)malloc(sizeof(int) * n * 2);
    
    for(int i = 0; i < n; i++){
        ans[i] = nums[i];
        ans[i + n] = nums[i];
    }

    *newSize = n * 2;
    return ans;
}
