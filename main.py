from medium import Medium
from node import Node
from state import State
import time
import threading

def main():
    state = State()
    medium = Medium(state)
    nodes = [Node(i, medium, state) for i in range(5)]
    
    threads = []
    timeout = 10
    # 运行统计器

    
    for node in nodes:
        thread = threading.Thread(target=node.run)
        threads.append(thread)
        thread.start()
    
        timer = threading.Timer(timeout, node.stop)
        timer.start()
       
    thread = threading.Thread(target=state.aggregate_result)
    threads.append(thread)
    thread.start()
    timer = threading.Timer(timeout, state.stop)
    timer.start()
    
    for thread in threads:# 等待所有线程完成 
        thread.join()
        
if __name__ == "__main__":
    main()