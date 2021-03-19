class Solution:
    def max_heap(self, arr, k, root):
        left = 2 * root + 1
        right = left + 1
        larger = root

        if left < k and arr[left] > arr[larger]:
            larger = left
        if right < k and arr[right] > arr[larger]:
            larger = right
        if larger != root:
            arr[root], arr[larger] = arr[larger], arr[root]
            self.max_heap(arr, k, larger)

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        for i in range(k//2-1, -1, -1):
            self.max_heap(arr, k, i)
        for j in range(k, len(arr)):
            if arr[j] < arr[0]:
                arr[j], arr[0] = arr[0], arr[j]
                self.max_heap(arr, k, 0)
        return arr[:k]
