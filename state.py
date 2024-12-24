import numpy as np

class State:
    def __init__(self):
        broadcast_info = np.zeros((5, 5))
        broadcast_trans = [1, 1, 1, 1, 1]
        self.trans = broadcast_trans
        self.info = broadcast_info