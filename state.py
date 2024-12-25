import numpy as np
from tabulate import tabulate
import time
import os
class State:
    def __init__(self):
        self.broadcast_info = [0, 0, 0, 0, 0]
        self.node_state = [0, 0, 0, 0, 0]# 0 表示初始化完毕的等待，1表示检测到信道忙，随机等待， 2表示开始发送， 3表示检测到冲突，随机后退， 4表示发送成功
        self.send_num = [0, 0, 0, 0, 0]
        self.state_running = 1
    def show_node_state(self):
        node_state = []
        node_state.append("node state:")
        for i in range(len(self.node_state)):
            if self.node_state[i] == 0:
                node_state.append("Initialized")
            elif self.node_state[i] == 1:
                node_state.append("Medium busy")
            elif self.node_state[i] == 2:
                node_state.append("Start sending")
            elif self.node_state[i] == 3:
                node_state.append("Collision")
            else:
                node_state.append("Send success")
        return node_state
    
    def show_send_num(self):
        send_num = []
        send_num.append("send num:")
        send_num.extend(self.send_num)
        return send_num
    
    def show_broadcast_state(self):
        broadcast_info = []
        broadcast_info.append("broadcast_info:")
        broadcast_info.extend(self.broadcast_info)
        return broadcast_info
    
    def aggregate_result(self):
        while self.state_running == 1:
            os.system('cls')
            headers = [" ","Node 0", "Node 1", "Node 2", "Node 3", "Node 4"]
            node_state = self.show_node_state()
            send_num = self.show_send_num()
            broadcast_info = self.show_broadcast_state()
            print(tabulate([node_state, send_num, broadcast_info], headers=headers, tablefmt='fancy_grid'))
            print('\n')
            time.sleep(0.05)
            
    
    def stop(self):
        self.state_running = 0
        