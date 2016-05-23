


class node(object):
    def __init__(self, x, y, name="", z=0):
        self.x = x
        self.y = y
        self.name = name
        self.z = z

class nodes(list):

    def __init__(self):
        super().__init__()

    def add_node(self, node_obj):
        self.append(node_obj)



