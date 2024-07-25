class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        mergeSort(nums, 0, nums.size() - 1);
        return nums;
    }
    void merge(vector<int>& arr, int left, int mid, int right){
        int subarr1 = mid - left + 1;
        int subarr2 = right - mid;
        vector<int> leftarr (subarr1);
        vector<int> rightarr (subarr2);

        for(int i = 0; i < subarr1; i++ ){
            (leftarr)[i] = arr[left + i];
        }
        for (int j = 0; j < subarr2; j++){
            (rightarr)[j] = arr[mid + 1 + j];
        }
        int index_of_subarr1 = 0, index_of_subarr2 = 0;
        int index_of_merged_arr = left;

        while (index_of_subarr1 < subarr1 && index_of_subarr2 < subarr2){
            if ((leftarr)[index_of_subarr1] <= (rightarr)[index_of_subarr2]){
                arr[index_of_merged_arr] = (leftarr)[index_of_subarr1];
                index_of_subarr1++;
            }
            else{
                arr[index_of_merged_arr] = (rightarr)[index_of_subarr2];
                index_of_subarr2++;
            }
            index_of_merged_arr++;
        }

        //if anything is left
        while(index_of_subarr1 < subarr1){
            arr[index_of_merged_arr] = (leftarr)[index_of_subarr1];
            index_of_merged_arr++;
            index_of_subarr1++;
        }

        while(index_of_subarr2 < subarr2){
            arr[index_of_merged_arr] = (rightarr)[index_of_subarr2];
            index_of_merged_arr++;
            index_of_subarr2++;
        }

        //delete leftarr;
        //delete rightarr;
    }

    void mergeSort(vector<int>& arr, int begin, int end){
        if (begin >= end){
            return;
        }
        int mid = begin + (end - begin) / 2;
        mergeSort(arr, begin, mid);
        mergeSort(arr, mid + 1, end);
        merge(arr, begin, mid, end);
    }
};