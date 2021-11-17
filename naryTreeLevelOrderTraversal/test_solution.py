from core.dataStructure.naryTree import Node
from .solution import Solution


def test_number_of_bits():
    import os
    from collections import deque

    FOLDER = "/Users/darya.bulanova/Downloads"
    files_total = 0
    dirs_total = 0
    queue = deque([FOLDER])
    while queue:
        dir_ = queue.popleft()
        files = os.listdir(dir_)
        for file in files:
            if file.endswith("/"):
                queue.append(file)
                dirs_total += 1
            else:
                if file.endswith('.parquet'):
                    files_total += 1
    print(f"dirs files={dirs_total}")
    print(f"total files={files_total}")
    # root = Node(val=1)
    # root.children = [Node(val=3, children=[Node(val=5), Node(val=6)]), Node(val=2), Node(val=4)]
    #
    # actual = Solution().levelOrder(root)
    # assert actual == [[1], [3, 2, 4], [5, 6]]
