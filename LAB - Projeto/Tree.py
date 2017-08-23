from Node import *

# Modified version of a BinaryTree to read and build a tree based on indented text file,

class Tree:

	def __init__(self):
		self.root = None

	def NewInsert(self, z, side, data):
		if side == "<":
			z.SetLeft(data)
			data.SetParent(z)
			return z.GetLeft()
		else:
			z.SetRight(data)
			data.SetParent(z)
			return z.GetRight()

	def Search(self, data, root):
		if root != None:
			if root.GetVar() == data:
				return root
			self.Search(data, root.GetLeft())
			self.Search(data, root.GetRight())

	def GetRoot(self):
		return self.root

	def SetRoot(self, root):
		self.root = root
		return self.root

	def Walk(self, node, val):
		if val < node.GetVal():
			node = node.GetLeft()
		else:
			node = node.GetRight()
		return node


	# DEBUG AREA -> FUNCTIONS USED FOR DEBUGGING THE PROGRAM
	def TreeWalk(self):
		self.InorderTreeWalk(self.root)

	def InorderTreeWalk(self, root):
		if root != None:
			self.InorderTreeWalk(root.GetLeft())
			print("%s    <-    %s    ->    %s" % (root.GetLeft(), root, root.GetRight()))
			self.InorderTreeWalk(root.GetRight())