class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap={i:[] for i in range(numCourses)}
        for c1,c2 in prerequisites:
            premap[c1].append(c2)
        visit=set()

        def dfs(crs):
            if crs in visit:
                return False
            if premap[crs]==[]:
                return True
            visit.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            premap[crs]=[]
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

