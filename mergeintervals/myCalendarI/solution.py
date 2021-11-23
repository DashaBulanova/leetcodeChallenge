class MyCalendar:

    def __init__(self):
        self.events = []

    def __has_overlap(self, event, start, end) -> bool:
        if event[1] <= start or end <= event[0]:
            return False
        return True

    def __get_insert_index(self, start: int, end: int) -> int:
        if len(self.events) == 0:
            return 0

        for i in range(len(self.events)):  # use binary search here
            event = self.events[i]

            if self.__has_overlap(event, start, end):
                return -1
            if event[0] > start:
                return i

        return len(self.events)

    def book(self, start: int, end: int) -> bool:
        insert_index = self.__get_insert_index(start, end)

        if insert_index == -1:
            return False

        if insert_index == len(self.events):
            self.events.append([start, end])
        else:
            self.events.insert(insert_index, [start, end])
        return True
