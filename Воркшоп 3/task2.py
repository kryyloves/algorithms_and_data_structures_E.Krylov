# реализация мин кучи, подумал нужна
class Min_Heap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        # добавляем в конец и поднимаем вверх
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        # если в куче больше 1 элемента, заменяем корень последним и опускаем
        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop()
            self._sift_down(0)
        else:
            self.heap.pop()

    def _sift_up(self, i):
        parent = (i - 1) // 2
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self._sift_up(parent)

    def _sift_down(self, i):
        smallest = i
        left, right = 2 * i + 1, 2 * i + 2
        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
            
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._sift_down(smallest)

def find_theBiggest_K (nums, k):
    h = Min_Heap()
    for n in nums:
        h.push(n)
        if len(h.heap) > k:
            h.pop()
    return h.heap[0]

assert find_theBiggest_K([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4