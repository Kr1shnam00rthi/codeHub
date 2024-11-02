class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence=sentence.split(" ")
        start=sentence[0]
        for i in range(1,len(sentence)):
            if start[-1]!=sentence[i][0]:
                return False
            start=sentence[i]
        if sentence[-1][-1]!=sentence[0][0]:
            return False
        return True
