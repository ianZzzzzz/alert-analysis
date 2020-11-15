import treelib
from treelib import Tree, Node


t = Tree ()
t.create_node(0,0,data = [])
# 0
a0 = [15,16,17,55,69,70,71]
for i in a0 :
    t.create_node(i,i,parent = 0,data=[])

# 15

a15 = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 72]
for i in a15:
    t.create_node(i,i,parent = 15,data=[])

# 16
for i in range(31,55):
    t.create_node(i,i,parent = 16,data=[])

t.show()
"""  
node = Node(data=50)
tree.add_node(node, parent='node-5')
node_a = Node(tag='Node-A', identifier='node-A', data='A')
tree.add_node(node_a, parent='node-5')


tree.show()
print(tree.identifier) """
