import treelib
from treelib import Tree, Node

tree = Tree()

tree.create_node(tag='AREA-0', identifier='area-0', data=100)
tree.create_node(tag='AREA-15', identifier='area-15', parent='area-0', data=200)
tree.create_node('AREA-16', 'area-16',parent='area-0', data=10)
tree.create_node('AREA-17', 'area-17',parent='area-0', data=13)

tree.create_node('AREA-72', 'area-72',parent='area-15', data=190)

tree.show()
"""  
node = Node(data=50)
tree.add_node(node, parent='node-5')
node_a = Node(tag='Node-A', identifier='node-A', data='A')
tree.add_node(node_a, parent='node-5')


tree.show()
print(tree.identifier) """
