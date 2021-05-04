class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        table = {0:0}
        for level in wall:
            tmp = 0
            for i in level[:-1]:
                tmp += i
                table[tmp] = table.get(tmp, 0) + 1
        return len(wall) - max(table.values())
