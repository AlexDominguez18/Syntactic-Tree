from node import Node
from stack import Stack

#DefVar -> type id VarList ;
class DefVar(Node):
    
    def __init__(self, stack):
        stack.pop()
        stack.pop()
        stack.pop()
        self.varList = stack.pop()
        self.id = Expression(stack)
        stack.pop()
        self.type = stack.pop()

#DefFunc -> type id ( Parameters ) BloqFunc
class DefFunc(Node):

    def __init__(self, stack):
        stack.pop()
        self.bloqFunc = stack.pop()
        stack.pop() #Number
        stack.pop() #)
        stack.pop() #Number
        self.parameters = stack.pop()
        stack.pop() #Number
        stack.pop() #)
        stack.pop() #Number
        self.id = stack.pop()
        stack.pop() #Number
        self.type = stack.pop()

#Parameters -> type id ParamList
class Parameters(Node):

    def __init__(self, stack):
        stack.pop() #Number
        self.paramList = stack.pop()
        stack.pop() #Number
        self.id = stack.pop()
        stack.pop() #Number
        self.type = stack.pop()

#VarList -> , id varList
class VarList(Node):

    def __init__(self, stack):
        stack.pop() #Number
        self.varList = stack.pop()
        stack.pop() #Number
        self.id = stack.pop()
        stack.pop() #Number
        stack.pop() #Comma

#ParamList -> , type id ParamList
class ParamList(Node):

    def __init__(self, stack):
        stack.pop() #Number
        self.paramList = stack.pop()
        stack.pop() #Number
        self.id = stack.pop()
        stack.pop() #Number
        self.type = stack.pop()
        stack.pop() #Number
        stack.pop() #Comma

#Assigment -> id = Expression ;
class Assignment(Node):

    def __init__(self, stack):
        stack.pop() #Number
        stack.pop() #Semicolon
        stack.pop() #Number
        self.expression = stack.pop()
        stack.pop() #Number
        self.operator = stack.pop() #=
        self.id = Expression(stack)

#if -> if ( Expression ) BlockSentence Other
class If(Node):

    def __init__(self, stack):
        stack.pop() #Number
        self.other = stack.pop()
        stack.pop() #Number
        self.blockSentence = stack.pop()
        stack.pop() #Number
        stack.pop() #)
        stack.pop() #Number
        self.expression = stack.pop()
        stack.pop() #Number
        stack.pop() #(
        stack.pop() #Number
        self.ifToken = stack.pop()

#while -> while ( Expression ) Block
class While(Node):

    def __init__(self, stack):
        stack.pop() #Number
        self.block = stack.pop()
        stack.pop() #Number
        stack.pop() #)
        stack.pop() #Number
        self.expression = stack.pop()
        stack.pop() #Number
        stack.pop() #(
        stack.pop() #Number
        self.whileToken = stack.pop()

#return -> return Expression ;
class Return(Node):

    def __init__(self, stack):
        stack.pop() #Number
        stack.pop() #Semicolon
        stack.pop() #Number
        self.expression = stack.pop()
        stack.pop() #Number
        stack.pop() #Return

#Expresion -> ID, TYPE or CONST
class Expression(Node):

    def __init__(self, stack):
        stack.pop()
        self.token = stack.pop()

#FunCall -> id ( params )
class FunCall(Node):

    def __init__(self, stack):
        stack.pop() #Number
        stack.pop() #)
        stack.pop() #Number
        self.params = stack.pop()
        stack.pop() #Number
        stack.pop() #(
        self.id = Expression(stack)

#Operation -> expression operator expression
class Operation(Node):

    def __init__(self, stack):
        stack.pop() #Number
        self.left = stack.pop() #Left exp
        stack.pop() #Number
        self.op = stack.pop() #Operator
        stack.pop() #Number
        self.right = stack.pop() #Right exp