class Node:

	def __init__(self, var, val):
		self.val = val
		self.var = var
		self.left = self.right = self.parent = self.data = None

	def __repr__(self):
		return str(self.var) + ": " + str(self.val)

	def GetVar(self):
		return self.var

	def GetVal(self):
		return self.val

	def GetData(self):
		return self.data

	def GetLeft(self):
		return self.left

	def GetRight(self):
		return self.right

	def GetParent(self):
		return self.parent

	def SetData(self, newdata):
		self.data = newdata

	def SetRight(self, newright):
		self.right = newright

	def SetLeft(self, newleft):
		self.left = newleft

	def SetParent(self, newparent):
		self.parent = newparent