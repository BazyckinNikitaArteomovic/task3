import heap
import linked_list
import matplotlib.pyplot as plt
import datetime
from statistics import mean


def insert_test(pq):
    pq.insert(1, 1)


def extract_test(pq):
    pq.extract_max()


sizes = [10000, 20000, 30000, 40000, 50000]
times = []
temp_times = []
number = 100
list_or_heap = int(input("Выберите связаный список или куча:\nСвязный список - 1\nКуча - 2\n"))
insert_or_extract = int(input("Выберите вставка или извлечение:\nВставка - 1\nИзвлечение - 2\n"))
if list_or_heap == 1:
    temp = 'linked_list.PriorityQueueLinkedList()'
else:
    temp = 'heap.PriorityQueueHeap()'
if insert_or_extract == 1:
    insert_or_extract = 'insert_test'
else:
    insert_or_extract = 'extract_test'

for size in sizes:
    temp_times = []
    for i in range(number):
        if 'list' in temp:
            list_or_heap = linked_list.PriorityQueueLinkedList()
        else:
            list_or_heap = heap.PriorityQueueHeap()
        for j in range(size):
            list_or_heap.insert(j, j)
        if 'insert' in insert_or_extract:
            start = datetime.datetime.now()
            insert_test(list_or_heap)
            finish = datetime.datetime.now()
        else:
            start = datetime.datetime.now()
            extract_test(list_or_heap)
            finish = datetime.datetime.now()
        temp_times.append((finish-start).microseconds)
    time = sum(temp_times) / len(temp_times)
    times.append(time)
    print(f'Size: {size}, Time: {time}')

plt.plot(sizes, times)

plt.xlabel("Размер входных данных")
plt.ylabel("Время выполнения (с)")
plt.title("График времени выполнения функции")

plt.show()
