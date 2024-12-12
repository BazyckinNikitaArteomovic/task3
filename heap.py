

class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, item, priority):
        self.heap.append((priority, item))
        self._bubble_up(len(self.heap) - 1)

    def extract(self):
        if not self.heap:
            raise IndexError("Извлечение из пустой кучи")
        root = self.heap[0]
        last_item = self.heap.pop()
        if self.heap:
            self.heap[0] = last_item
            self._bubble_down(0)
        return root[1]

    def _bubble_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index][0] < self.heap[parent_index][0]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._bubble_up(parent_index)

    def _bubble_down(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        if left_child < len(self.heap) and self.heap[left_child][0] < self.heap[smallest][0]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child][0] < self.heap[smallest][0]:
            smallest = right_child
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._bubble_down(smallest)


class PriorityQueueHeap:
    def __init__(self):
        self.heap = Heap()

    def insert(self, x, p):
        self.heap.insert(x, p)

    def extract_max(self):
        return self.heap.extract()


pq_heap = PriorityQueueHeap()
pq_heap.insert('A', 2)
pq_heap.insert('B', 5)
pq_heap.insert('C', 3)

print(pq_heap.extract_max())
print(pq_heap.extract_max())
print(pq_heap.extract_max())
