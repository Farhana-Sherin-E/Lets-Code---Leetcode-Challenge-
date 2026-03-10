class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        CL = 0
        CR = 0
        blank = 0

        for i in moves:
            if i == 'L':
                CL += 1
            elif i == 'R':
                CR += 1
            else:
                blank += 1

        return abs(CL - CR) + blank
