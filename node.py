import random
import time
from medium import Medium
from state import State
class Node:
    """
    node类：
        负责仿真节点
    """
    def __init__(self, node_id, Medium):
        super().__init__()
        self.node_id = node_id
        self.medium = Medium
        self.running = True
        self.state = State

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
        self.medium.transmission_exit(self.node_id)
        print(f"Node {self.node_id}: Random Backoff...")
        time.sleep(random.unifrom(1, 4))
    
    # def broadcast_info(self):
    #     "实现广播信道占用消息"
    #     copy_trans = self.state.broadcast_trans
    #     sorted_elements = []
    #     before = 0
    #     while copy_trans:
    #         min_value = min(copy_trans)
    #         indices = [i for i, x in enumerate(copy_trans) if x == min_value]
    #         sorted_elements.append((min_value, indices))
    #         my_list = [x for x in my_list if x != min_value]
    #     for value, positions in sorted_elements:
    #         if positions == self.node_id:
    #             continue
    #         time.sleep(value - before)
    #         self.collision_detect()
    #         before = value
    #         self.state.broadcast_info[self.node_id, positions] = 1
    #     if 5 - before > 0:
    #         time.sleep(5 - before)
        
        
    def send(self):
        self.medium.transmission_add(self.node_id)
        print(f"Node {self.node_id}: Sending Data...")
        #self.broadcast_info()
        time.sleep(1)
        while self.collision_detect():
            self.random_backoff()
            time.sleep(1)
        print(f"Node {self.node_id}: Send Success!")
        self.medium.transmission_exit(self.node_id)
        
    def run(self):
        while self.running:
            if self.busy_detect():# 检测到信道忙，等待一段时间
                self.random_waiting()# 随机等待
                continue
            else:
                self.send()# 发送
                return
                
    