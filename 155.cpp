#include<bits/stdc++.h>
class MinStack {
public:
    
    vector<int> nums;
    
    
    void push(int val) {
        nums.push_back(val);
    }
    
    void pop() {
        nums.pop_back();
    }
    
    int top() {
        return nums[nums.size()-1];
    }
    
    int getMin() {
        int min=nums[0];
        for(int i=1;i<nums.size();i++){
            if(nums[i]<min){
                min=nums[i];
            }
        }
        return min;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
