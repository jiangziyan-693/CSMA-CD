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
    def __init__(self, state):
        self.state = state
        print("信道初始化成功！")
        
    def is_busy(self):
        "判断信道是否繁忙"
        if self.state.broadcast_info.count(1) > 0:
            return True
        else:
            return False
    
    def collision_detect(self):
        "set内元素数量大于1"
        if self.state.broadcast_info.count(1) > 1:
            return True
        else:
            return False
    
