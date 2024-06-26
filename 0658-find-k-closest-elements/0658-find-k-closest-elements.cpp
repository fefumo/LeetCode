#include<vector>
#include <iostream>
#include <cmath>
#include "bits/stdc++.h"
using namespace std;

class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int n = arr.size();
        int pos = binarySearch(arr, n, x);
        int l = pos - 1, r = pos;

        vector<int> res;

        while(k > 0 && l >= 0 && r < n){
            if (abs(x - arr[l]) <= abs(x - arr[r])){
                res.push_back(arr[l--]);
            }
            else{
                res.push_back(arr[r++]);
            }
            k--;
        }

        while(k--){
            if (l < 0){
                res.push_back(arr[r++]);
            }
            else if( r >= n){
                res.push_back(arr[l--]);
            }
        }
        sort(res.begin(), res.end());
        return res;
    }
    int binarySearch(vector<int> &arr, int n, int x){
        if (arr[0] > x) return 0;
        int s = 0, e = n - 1, mid;
        while (s <= e){
            mid = s + (e - s) / 2;
            if (arr[mid] == x) return mid;
            else if (arr[mid] < x ) {
                s = mid + 1;
            }
            else{
              e = mid - 1;  
            } 
        }
        return s;
    }
};