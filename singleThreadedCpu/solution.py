from heapq import heapify, heappop


class SingleThreadCpu:
    def __init__(self, start_time):
        self.time = start_time
        self.execution_log = []

    def tick(self):
        self.time += 1

    def execute(self, id, processing_time):
        self.execution_log.append(id)
        self.time = self.time + processing_time


class Task:
    def __init__(self, id, start_time, processing_time):
        self.processing_time = processing_time
        self.start_time = start_time
        self.id = id

    def __lt__(self, other):
        if self.processing_time == other.processing_time:
            return self.id < other.id
        return self.processing_time < other.processing_time


class Solution:

    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        t = [Task(id=i, start_time=tasks[i][0], processing_time=tasks[i][1]) for i in range(len(tasks))]
        s_tasks = sorted(t, key=lambda x: (x.start_time, x.processing_time))
        # q = collections.deque(tasks)
        available = []
        pointer = 0
        heapify(t)
        cpu = SingleThreadCpu(s_tasks[pointer].start_time)
        while pointer < len(s_tasks) or available:
            while pointer < len(s_tasks) and cpu.time >= s_tasks[pointer].start_time:
                available.append(s_tasks[pointer])
                heapify(available)
                pointer += 1
            if available:
                task = heappop(available)
                cpu.execute(task.id, task.processing_time)

        return cpu.execution_log
