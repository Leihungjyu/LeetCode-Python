class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        table = {}
        for word in words:
            table[word] = table.get(word, 0) + 1
        table = sorted(table.items(), key = lambda x:(-x[1], x[0]))
        res = []
        for key, value in table[:k]:
            res.append(key)
        return res
        