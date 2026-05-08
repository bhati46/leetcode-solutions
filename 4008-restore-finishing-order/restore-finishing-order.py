class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        x=[]
        friends=set(friends)
        for i in range(len(order)):
            if order[i] in friends:
                x.append(order[i])
        return x