import random
import time
from medium import Medium
from state import State
class Node:
    """
    node类：
        负责仿真节点
    """
    def __init__(self, node_id, Medium, State):
        super().__init__()
        self.node_id = node_id
        self.medium = Medium
        self.running = True
        self.state = State
        print(f"Node {self.node_id}: 初始化成功！")

    def busy_detect(self):
        if self.medium.is_busy():
            return True
        else: 
            return False
    
    def random_waiting(self):
        print(f"Node {self.node_id}: Medium is busy, Waiting...")
        time.sleep(random.uniform(0.5, 2))
        
   
        
    def collision_detect(self):
        if self.medium.collision_detect():
            print(f"Node {self.node_id}: Collision Detect!")
            return True
        else:
            return False
    
    def random_backoff(self):
        print(f"Node {self.node_id}: Random Backoff...")
        time.sleep(random.uniform(1, 4))
        
        
    def send(self):
        print(f"Node {self.node_id}: Sending Data...")
        time.sleep(0.5)
        self.medium.transmission_add(self.node_id)
        time.sleep(0.5)
        while self.collision_detect():
            self.medium.transmission_exit(self.node_id)
            self.random_backoff()
            self.medium.transmission_add(self.node_id)
            time.sleep(1)
        print(f"Node {self.node_id}: Send Success!")
        self.medium.transmission_exit(self.node_id)
        
    def run(self):
        while self.running:
            time.sleep(random.uniform(1,3))
            if self.busy_detect():# 检测到信道忙，等待一段时间
                self.random_waiting()# 随机等待
                continue
            else:
                self.send()# 发送
                return
                
    