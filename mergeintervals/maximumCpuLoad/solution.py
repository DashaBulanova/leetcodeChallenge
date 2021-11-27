class job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

def find_max_cpu_load(jobs):
    starts = []
    ends = []

    for job in jobs:
        starts.append((job.start, job.cpu_load))
        ends.append((job.end, job.cpu_load))

    starts.sort(key=lambda x: x[0])
    ends.sort(key=lambda x: x[0])

    start_pointer, end_pointer = 0,0
    acc_cpu_load = 0
    max_cpu_load = 0
    while start_pointer < len(jobs):
        if starts[start_pointer][0] < ends[end_pointer][0]:
            acc_cpu_load += starts[start_pointer][1]
            max_cpu_load = max(max_cpu_load, acc_cpu_load)
            start_pointer +=1
        else:
            acc_cpu_load -= ends[end_pointer][1]
            end_pointer += 1

    return max_cpu_load
