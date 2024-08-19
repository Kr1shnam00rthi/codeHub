#include<bits/stdc++.h>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res;
        int count=0;
        for(int i=0;i<nums.size();i++){
            for(int j=0;j<nums.size();j++){
                if(i!=j && (nums[i]+nums[j])==target){
                    res.push_back(i);
                    res.push_back(j);
                    count+=1;
                    break;
                }
            }
            if(count==1){
                break;
            }
        }
        return res;
    }   
};
