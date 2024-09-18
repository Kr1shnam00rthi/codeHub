class TimeMap:

    def __init__(self):
        self.elements=dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        temp=[timestamp,value]
        if key not in self.elements:
            self.elements[key]=[temp]
        else:
            a=self.elements[key]
            a.extend([temp])
            self.elements[key]=a

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.elements:
            return ""

        a = self.elements[key]
        l, e = 0, len(a) - 1
        if timestamp < a[l][0]:
            return ""
        while l <= e:
            mid = (l + e) // 2
            if a[mid][0] <= timestamp:
                l = mid + 1  
            else:
                e = mid - 1 
        return a[e][1]

