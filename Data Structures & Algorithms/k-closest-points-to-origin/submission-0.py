import math
from typing import List
import heapq
class Solution:
    def euclidian_dist(self, point_1: List, point_2: List = [0,0]):
        if len(point_1) != len(point_2):
            return ValueError("Points must be same dimensions")
        return math.sqrt(sum((a - b)**2 for a, b in zip(point_1, point_2)))
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_dist = [-self.euclidian_dist(point) for point in points]
        pointsMaxHeap = list(zip(points_dist, points))
        heapq.heapify(pointsMaxHeap)
        while len(pointsMaxHeap) > k: 
            heapq.heappop(pointsMaxHeap)
        return [point for _, point in pointsMaxHeap]
        

        
        