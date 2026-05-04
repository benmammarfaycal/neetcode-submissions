class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        a=zip(position,speed)
        a=sorted(a,reverse=True)
        times=[]
        for i in range(len(speed)):
            time=(target-a[i][0])/a[i][1]
            times.append(time)
        time_fleet=0
        fleet=0
        for i in times:
            if i>time_fleet:
                time_fleet=i
                fleet+=1
        return fleet
        
