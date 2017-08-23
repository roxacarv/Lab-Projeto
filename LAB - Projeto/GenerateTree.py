from Tree import *
from Node import *

def BuildInputList(txt):
	listOf = []
	for t in txt:
		varval = t.split()
		if "|" in varval:
			bars = "".join([x for x in varval if "|" in x])
			varval = [x for x in varval if "|" not in x and "(" not in x and "[" not in x]
			varval = [bars] + varval
		listOf.append(varval)
	return listOf, len(txt)

def BuildTree(InputList, m):
	AllocTree = Tree()
	CurrentNode, n, this = None, 0, None
	than, indent = "", ""
	while n < m:
		if "|" not in InputList[n] and AllocTree.GetRoot() == None:
			this = AllocTree.SetRoot(Node(InputList[n][0], float(InputList[n][2])))
			than = InputList[n][1]
			indent = InputList[n][0].count("|")
		else:
			if InputList[n][0].count("|") > indent:
				this = AllocTree.NewInsert(this, than, Node(InputList[n][1], float(InputList[n][3])))
				than = InputList[n][2]
				indent = InputList[n][0].count("|")
				if len(InputList[n]) > 4 and InputList[n][4] == ":":
					if InputList[n][2] == "<":
						this.SetLeft(Node("leaf", InputList[n][5]))
					else:
						this.SetRight(Node("leaf", InputList[n][5]))
			elif InputList[n][0].count("|") == indent:
				if len(InputList[n]) > 4 and InputList[n][4] == ":":
					if InputList[n][2] == "<":
						this.SetLeft(Node("leaf", InputList[n][5]))
					else:
						this.SetRight(Node("leaf", InputList[n][5]))
				than = InputList[n][2]
			elif InputList[n][0].count("|") < indent:
				indent = indent - InputList[n][0].count("|")
				c = 0
				while indent > c:
					this = this.GetParent()
					c += 1
				if len(InputList[n]) > 4 and InputList[n][4] == ":":
					if InputList[n][2] == "<":
						this.SetLeft(Node("leaf", InputList[n][5]))
					else:
						this.SetRight(Node("leaf", InputList[n][5]))
				indent = InputList[n][0].count("|")
				than = InputList[n][2]

		n += 1
	return AllocTree