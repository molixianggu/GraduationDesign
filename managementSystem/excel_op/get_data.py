import xlrd



class execl(object):

    def __init__(self, file_name):
        self.obj = xlrd.open_workbook(file_name)


    def contrast(self, obj, nodes):
        for node in nodes:
            table1 = self.obj.sheets()[node.z]
            table2 = obj.obj.sheets()[node.z]
            val1 = table1.col_values(node.x)[node.y]
            val2 = table2.col_values(node.x)[node.y]
            if val1 != val2:
                print("({x},{y}) [{name}] {a}  >>>  {b}".format(
                    x=node.x, y=node.y, name=node.name, a=val1, b=val2)
                )
        # for table in self.obj.sheets():
        #     print(table.nrows)
        #     print(table.ncols)

            # print(table.col_values(0))
            # print(table.col_values(1))
            # print(table.col_values(2))




        # name = table.col_values(0)
        # k = table.col_values(1)
        # m = table.col_values(2)

from location import nodes, node


n = nodes()
n.add_node(node(2, 0, "中"))
n.add_node(node(2, 1, "省道"))
n.add_node(node(2, 2, "吧"))
n.add_node(node(2, 3, "额"))
n.add_node(node(2, 4, "百度"))
n.add_node(node(2, 5, "省的道"))
n.add_node(node(2, 6, "好烦的"))
n.add_node(node(2, 7, "说的"))
n.add_node(node(2, 8, "部分"))
n.add_node(node(2, 9, "水电费"))
n.add_node(node(2, 10, "而已"))
n.add_node(node(2, 11, "请问"))
n.add_node(node(2, 12, "请额"))
n.add_node(node(2, 13, "of的"))

ex = execl("t.xlsx")
et = execl("t2.xlsx")

ex.contrast(et, n)
