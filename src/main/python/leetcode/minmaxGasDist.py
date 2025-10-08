import heapq
class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        
        gaps = [stations[i]-stations[i-1] for i in range(1,len(stations))]
        total_gap = sum(gaps)
        avg_k_spacing = total_gap*1.0/(k+1)
        
        gap_added = [ math.floor(g/avg_k_spacing) for g in gaps ]
        remainder = k-sum(gap_added)

        heap = [ (-gaps[i]/(gap_added[i]+1), gaps[i], gap_added[i]) for i in range(len(gaps)) ]
        heapq.heapify(heap)
        
        while remainder:
            previous_penalty, gap, added = heapq.heappop(heap)
            added += 1
            heapq.heappush(heap, (-gap/(added+1), gap, added))
            remainder -= 1

        penalty, gap, added = heapq.heappop(heap)
        return -penalty
