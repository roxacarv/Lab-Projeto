from GenerateTree import BuildTree, BuildInputList
import os

def ClearConsole():
	os.system('cls' if os.name == 'nt' else 'clear')

def Interface(BaseNode, interface=True):
	global TreeString
	if interface:
		print("           _______________________________")
		print("          |                               |")
		print("          | BEM VINDO A ÁRVORE DE DECISÃO |\n" +
			  "          | Para começar, escolha uma das |\n" + 
			  "          | opções abaixo;                |\n" +
			  "          |_______________________________|\n")
		print("             (1) - Caminhar pela Árvore\n" +
			  "             (2) - Resetar Caminhada\n" +
			  "             (3) - Ver Caminho\n" + 
			  "             (4) - Sair\n\n" +
			  "             Nó Atual --> %s\n\n" % str(BaseNode).upper())
	else:
		print("           _______________________________")
		print("          |                               |")
		print("          |      CAMINHO PERCORRIDO       |\n" +
			  "          |_______________________________|\n")
		TreeString = TreeScreen(BaseNode, TreeString)
		print(TreeString)


def TreeScreen(BaseNode, BaseString):
	if BaseNode.GetParent() == None:
		temp = BaseString
		BaseString = temp + "                      [%s]\n" % DT.GetRoot() 
	else:
		if BaseNode == BaseNode.GetParent().GetLeft():
			temp = BaseString
			BaseString = temp + "[%s]    \n" % str(BaseNode)
		else:
			temp = BaseString
			BaseString = temp + "    [%s]\n" % str(BaseNode)
	return BaseString


def WalkInTree(bnode):
	ClearConsole()
	Interface(bnode, False)
	print("   Digite o valor de uma variável: ", end="")
	Input = float(input())
	return DT.Walk(bnode, Input)

def Initialize(BaseNode):
	Interface(BaseNode)
	print("   Escolha: ", end="")
	Input = input()
	if Input == "1":
		BaseNode = WalkInTree(BaseNode)
		ClearConsole()
		Initialize(BaseNode)
	elif Input == "2":
		Initialize(DT.GetRoot())
	else:
		print("Escolha 3")

with open("arvore-teste.txt", 'r') as f:
	txt_lines, lines = BuildInputList(f.readlines())
	DT = BuildTree(txt_lines, lines)

TreeString = ""
Initialize(DT.GetRoot())