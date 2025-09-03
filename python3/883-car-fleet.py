class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sp = list(zip(position, speed))
        # for i in range(len(position)):
        #     sp.append([position[i], speed[i]])
        
        sp.sort(reverse=True)
        last_t = (target - sp[0][0])/sp[0][1]
        fleets = 1
        for [p, s] in sp[1:]:
            new_t = (target - p)/s
            # print(p, s, new_t, last_t)
            if new_t > last_t:
                fleets += 1
                last_t = new_t
        
        return fleets
