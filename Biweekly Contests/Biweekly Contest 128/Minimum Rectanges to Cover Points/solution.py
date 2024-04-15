class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        if(len(points) == 0):
            return 0
        x_list = [item[0] for item in points]
        x_list.sort()
        last_w = x_list[0]
        rects = 1
        for x_p in x_list:
            if x_p > last_w + w:
                last_w = x_p
                rects += 1
        return rects
