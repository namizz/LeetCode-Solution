class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = [0] * len(boxes)        
        moves = 0
        count = 0
        for i in range(len(boxes)):
            result[i] += moves
            count += int(boxes[i])  
            moves += count          
        moves = 0
        count = 0
        for i in range(len(boxes) - 1, -1, -1):
            result[i] += moves
            count += int(boxes[i]) 
            moves += count
        return result