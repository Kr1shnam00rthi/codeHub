class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end());
        auto it=nums.end()-k;
        return *(it);     
    }
};
