from medium import Medium
from node import Node
import time
import threading
def main():
    medium = Medium()
    nodes = [Node(i, medium) for i in range(5)]

    threads = []

    for node in nodes:
        thread = threading.Thread(target=node.run)
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()