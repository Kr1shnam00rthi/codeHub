class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count=0
        l=0
        e=len(people)-1
        while len(people)!=0:
            if len(people)==1:
                count+=1
                return count
            if people[l]+people[e]<=limit:
                count+=1
                people.pop(0)
                people.pop()
                l=0
                e=len(people)-1
            else:
                count+=1
                people.pop()
                e=len(people)-1
        return count
                    
