/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* singleNumber(int* nums, int numsSize, int* returnSize) {
    int xor = 0, *ans = (int *)calloc(1, sizeof(int) * 2), bitmask;
    *returnSize = 2;
    for (int i = 0; i < numsSize; i++) {
        xor ^= nums[i];
    }

    /* First set bit in XOR */
    for (int i = 0; i < 31; i++) {
        if ((1 << i) & xor) {
            bitmask = (1 << i);
            break;
        }
    }

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] & bitmask) {
            ans[0] ^= nums[i];
        }
        else {
            ans[1] ^= nums[i];
        }
    }
    return ans;
}