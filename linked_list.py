class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None


class PriorityQueueLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, x, p):
        new_node = Node(x, p)
        if self.head is None or self.head.priority < p:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.priority >= p:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def extract_max(self):
        if self.head is None:
            raise IndexError("Очередь пуста")
        max_node = self.head
        self.head = self.head.next
        return max_node.data


pq_linked_list = PriorityQueueLinkedList()
pq_linked_list.insert('A', 2)
pq_linked_list.insert('B', 5)
pq_linked_list.insert('C', 3)

print(pq_linked_list.extract_max())
print(pq_linked_list.extract_max())
print(pq_linked_list.extract_max())
