class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)

        for n in hand:
            start = n
            while count.get(start-1, 0):
                start -= 1
            
            while start <= n:
                if count[start]:
                    print(start)
                    for i in range(start, start + groupSize):
                        if count[i]:
                            count[i] -= 1
                        else:
                            return False
                else:
                    start += 1
        
        return True