class Solution:
    def permutation(self, s: str) -> List[str]:
        def func(x):
            func_set = set()
            if x == len(array) - 1:
                ans.append("".join(array))

                return

            for i in range(x, len(array)):
                if array[i] not in func_set:
                    func_set.add(array[i])
                    array[i], array[x] = array[x], array[i]
                    func(x + 1)
                    array[i], array[x] = array[x], array[i]

        array, ans = list(s), list()
        func(0)

        return ans
