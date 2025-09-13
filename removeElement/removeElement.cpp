// Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
// The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>

using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        if (nums.empty()) {
            return 0;
        }
        int k = 0;
        int length = nums.size();

        while (k < nums.size()) {
            if (nums[k] == val) {
                nums.erase(nums.begin() + k);
            }
            else {
                k++;
            }
        }
        return k;
    }
};

int main()
{
    Solution sol;

    vector<int> nums1 = { 3, 2, 2, 3 };
    vector<int> nums2 = { 0,1,2,2,3,0,4,2 };

    int val1 = 3;
    int val2 = 2;

    vector<int> expectedNums1 = { 2, 2 };
    vector<int> expectedNums2 = { 0, 1, 3, 0, 4 };

    int k1 = sol.removeElement(nums1, val1);
    int k2 = sol.removeElement(nums2, val2);

    assert(k1 == expectedNums1.size());
    assert(k2 == expectedNums2.size());

    sort(nums1.begin(), nums1.begin() + k1);
    sort(expectedNums1.begin(), expectedNums1.end());
    for (int i = 0; i < k1; i++) {
        assert(nums1[i] == expectedNums1[i]);
    }

    sort(nums2.begin(), nums2.begin() + k2);
    sort(expectedNums2.begin(), expectedNums2.end());
    for (int i = 0; i < k2; i++) {
        assert(nums2[i] == expectedNums2[i]);
    }

    cout << k1 << ": ";
    for (int i = 0; i < k1; i++) {
        cout << nums1[i] << " ";
    }
    cout << endl;

    cout << k2 << ": ";
    for (int i = 0; i < k2; i++) {
        cout << nums2[i] << " ";
    }
    cout << endl;

    return 0;

}