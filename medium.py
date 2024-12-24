import time
import random
class Medium():
    """
    medium类：
    负责作为仿真信道，统计信道的占用情况，可以实现的功能：
    · 判断信道是否繁忙
    · 节点加入信道
    · 判断信道是否有冲突
    · 节点退出信道
    """
    def __init__(self):
        self.node_in_medium = set()
        print("信道初始化成功！")
        
    def is_busy(self):
        "判断信道是否繁忙"
        if len(self.node_in_medium) > 0:
            return True
        else:
            return False
    
    def transmission_add(self, node_id):
        "让一个节点占用信道"
        self.node_in_medium.add(node_id)
        print(f"Node {node_id}:加入信道")
    
    def collision_detect(self):
        "set内元素数量大于1"
        if len(self.node_in_medium) > 1:
            return True
        else:
            return False
        
    def transmission_exit(self, node_id):
        "节点退出信道"
        self.node_in_medium.remove(node_id)
    
