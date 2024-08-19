#include<bits/stdc++.h>
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        nums1.insert(nums1.end(),nums2.begin(),nums2.end());
        sort(nums1.begin(),nums1.end());
        int length=nums1.size();
        double res=0.0;
        if(length%2 ==0){
            res=(nums1[length/2]+nums1[(length/2)-1])/double(2);
            
        }
        else{
            res=double(nums1[length/2]);
        }
        return res;
    }
};
