class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        end=paths[0][1]
        while True:
            c=0
            for i in range(len(paths)):
                if paths[i][0]==end:
                    end=paths[i][1]
                    c=1
            if c==0:
                return end
        return end
