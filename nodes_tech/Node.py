from typing import Any
from TypeNodes import TypeNodes

class Node:
    def __init__(self, id: int, name: str, type: TypeNodes, position: tuple[int, int]):
        self.id = id
        self.correlates = []
        self.name = name
        self.size = 0
        self.type = type
        self.position = position

   
    def add_correlation(self, node_id: int):
        if node_id == self.id:
            return
        
        if node_id not in self.correlates:
            self.correlates.append(node_id)
            self.set_size()

    def remove_correlation(self, node_id: int):
        if node_id in self.correlates:
            self.correlates.remove(node_id)
            self.set_size()

    def set_size(self):
        self.size = len(self.correlates)

    def get_position(self):
        return self.position

    def get_id(self):
        return self.id

    def get_correlates(self):
        return self.correlates

    def get_size(self):
        return self.size
