class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        y=0
        x=len(cost)
        for i in range(0,x,3):
            if i + 1 < x:
                y += cost[i] + cost[i+1]
            else:
                y += cost[i]
        return y