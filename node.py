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
        #print(f"Node {self.node_id}: Medium is busy, Waiting...")
        time.sleep(random.uniform(0.5, 2))
        
   
        
    def collision_detect(self):
        if self.medium.collision_detect():
            #print(f"Node {self.node_id}: Collision Detect!")
            return True
        else:
            return False
    
    def random_backoff(self):
        #print(f"Node {self.node_id}: Random Backoff...")
        time.sleep(random.uniform(1, 4))
        
        
    def send_data(self):
        self.state.node_state[self.node_id] = 2
        #print(f"Node {self.node_id}: Sending Data...")
        time.sleep(0.5)
        self.state.broadcast_info[self.node_id] = 1
        time.sleep(0.5)
        while self.collision_detect():
            self.state.node_state[self.node_id] = 3
            self.state.broadcast_info[self.node_id] = 0
            self.random_backoff()
            self.state.broadcast_info[self.node_id] = 1
            time.sleep(1)
        #print(f"Node {self.node_id}: Send Success!")
        self.state.node_state[self.node_id] = 4
        time.sleep(1)
        self.state.send_num[self.node_id] += 1
        self.state.broadcast_info[self.node_id] = 0
        
    def run(self):
        while self.running:
            if self.state.node_state[self.node_id] == 4:
                self.state.node_state[self.node_id] = 0
            time.sleep(random.uniform(1,3))
            if self.busy_detect():# 检测到信道忙，等待一段时间
                self.state.node_state[self.node_id] = 1
                self.random_waiting()# 随机等待
                continue
            else:
                self.send_data()# 发送
                
    def stop(self):
        self.running = False
        return