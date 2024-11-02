class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        for i in range(len(intervals)):
            for j in range(0,len(intervals)-i-1):
                if intervals[j][0]>intervals[j+1][0]:
                    intervals[j],intervals[j+1]=intervals[j+1],intervals[j]
        stack=[intervals[0]]
        for i in range(1,len(intervals)):
            if stack[-1][1]>=intervals[i][0]:
                if stack[-1][1]<intervals[i][1]:
                    stack[-1][1]=intervals[i][1]
            else:
                stack.append(intervals[i])
        return stack
