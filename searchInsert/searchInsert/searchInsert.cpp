#include <iostream>
#include <vector>
using namespace std;

// Class to solve the "Search Insert Position" problem.

class Solution {
public:
    /**
        Find the index of target in nums, or the position where it should be inserted.
        Uses binary search.
     
        @param nums   Sorted vector of integers.
        @param target Value to search for.
        @return Index of target, or insert position.
     */
    int searchInsert(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;

        while (low <= high) {
            int mid = (high - low) / 2;

            if (nums[mid] == target) {
                return mid;
            }
            else if (nums[mid] > target) {
                high = mid - 1;
            }
            else {
                low = mid + 1;
            }
        }
        return low; // Insert position
    }
};

int main() {
    Solution sol;
    vector<int> nums = { 1, 3, 5, 6 };

    cout << "Target = 2 --> Index: " << sol.searchInsert(nums, 2) << endl;
    cout << "Target = 5 --> Index: " << sol.searchInsert(nums, 5) << endl;
    cout << "Target = 7 --> Index: " << sol.searchInsert(nums, 7) << endl;
    cout << "Target = 0 --> Index: " << sol.searchInsert(nums, 0) << endl;

    return 0;
}