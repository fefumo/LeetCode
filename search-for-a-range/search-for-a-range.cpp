#include<vector>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        vector<int> result {};


        if (nums.size() == 1) {
            if (nums[0] == target) {
                return {0, 0};
            } else {
                return {-1, -1};
            }
        }

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                int fmin = mid; //we can actually use one variable for memory efficiency here. just reallocate this one after the first while loop:)
                int fmax = mid; //but i'm not gonna do that...

                while (fmin >= 0 && nums[fmin] == target) {
                    fmin--;
                }
                
                result.push_back(fmin + 1);

                while (fmax < nums.size() && nums[fmax] == target) {
                    fmax++;
                }
                
                result.push_back(fmax - 1);
                break;
            } 
            else if (nums[mid] > target) {
                right = mid - 1;
            }
            else {
                left = mid + 1;
            }
        }

        if (result.size() == 0) {
            result = {-1, -1};
        }

        return result;
    }
};