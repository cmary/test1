class Node(object):
	"""docstring for Node"""
	def __init__(self, arg):
		self.arg = arg
		self.lchild=Node
		self.rchild=Node

class Tree(object):
	"""docstring for Tree"""
	def __init__(self):
		self.root = Node

	def add(self,item):
		node=Node(item)
		if self.root is None:
			self.root=node
			return 
		queue = [self.root]
		while queue:
			cur_node =queue.pop(0)
			if cur_node.lchild is None:
				
		