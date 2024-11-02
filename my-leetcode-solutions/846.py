class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        while len(hand)!=0:
            a=min(hand)
            hand.remove(a)
            for _ in range(groupSize-1):
                if a+1 not in hand:
                    return False
                a=a+1
                hand.remove(a)
        return True
