import os
from rules import *
from stack import Stack
from node import Node

RIGHT = 1
LEFT = 0

class SyntacticAnalyzer():

    def __init__(self):
        self.table = []
        self.rules = []
        self.get_table()
        self.get_rules()
    
    def get_table(self):
        path_file = os.path.join(os.path.dirname(__file__), 'rules/GR2slrTable.txt')
        f = open(path_file, 'r')
        for line in f.readlines():
            self.table.append( [ int (x) for x in line.split('\t') ] )
        f.close()

    def get_rules(self):
        path_file = os.path.join(os.path.dirname(__file__), 'rules/GR2slrRulesId.txt')
        f = open(path_file, 'r')
        for line in f.readlines():
            self.rules.append( [ int (x) for x in line.split('\t') ] )
        f.close()
    
    def rulePops(self, rule, stack):
        #Special rules
        if rule == 5:
            node = DefVar(stack)
        elif rule == 7:
            node = VarList(stack)
        elif rule == 8:
            node = DefFunc(stack)
        elif rule == 10:
            node = Parameters(stack)
        elif rule == 12:
            node = ParamList(stack)
        elif rule == 20:
            node = Assignment(stack)
        elif rule == 21:
            node = If(stack)
        elif rule == 22:
            node = While(stack)
        elif rule == 23:
            node = Return(stack)
        elif rule == 33 or rule == 34:
            node = Expression(stack)
        elif rule == 35:
            node = FunCall(stack)
        elif rule == 39 or rule == 40 or rule == 41 or rule == 42:
            node = Operation(stack)
        #Rules that only generate one element
        elif rule == 0 or rule == 3 or rule == 4 or rule == 16 or \
            rule == 17 or rule == 32 or rule == 36 or rule == 37:
            stack.pop() #Number
            node = stack.pop() #Element
        #Rules that generate two elements
        elif rule == 24:
            stack.pop() #Number
            stack.pop() #Semicolon
            stack.pop() #Number
            node = stack.pop() #Function call
        elif rule == 26:
            stack.pop() #Number
            node = stack.pop() #Block sentence
            stack.pop() #Number
            stack.pop() #else
        elif rule == 13 or rule == 27 or rule == 38:
            stack.pop() #Number
            stack.pop() #} or )
            stack.pop() #Number
            #DefLocales or Sentences or Expression
            node = stack.pop()
            stack.pop() #Number
            stack.pop() #{
        elif rule == 2 or rule == 15 or rule == 19 or rule == 29:
            stack.pop() #Number
            aux = stack.pop() #Aux node
            stack.pop() #Number
            #Definitions or DefLocales or Sentences or ParamList
            node = stack.pop() 
            node.set_next(aux)
        elif rule == 31:
            stack.pop() #Number
            aux = stack.pop() #Aux node
            stack.pop() #Number
            node = stack.pop() #Expression
            node.set_next(aux)
            stack.pop() #Number
            stack.pop() #Comma
        else:
            node = Node()
        return node

    def is_accepted(self, code):
        #Creating the stack
        stack = Stack()
        #Initial push
        stack.push(0)
        #Analyzing
        i = 0
        while i < len(code):
            row = stack.top()
            column = code[i]['number']
            action = self.table[row][column]
            #Displacement case
            if action > 0:
                node = Node(code[i]['number'], code[i]['token'])
                stack.push(node)
                #print(f'{node.get_number()}, {node.get_token()}')
                stack.push(action)
                i += 1
            #Reduction case
            elif action < -1:
                ruleRow = (action * -1) - 1
                transition = self.rules[ruleRow][LEFT]
                node = self.rulePops(ruleRow, stack)
                row = stack.top() #Number
                newAction = self.table[row][transition]
                stack.push(node)
                stack.push(newAction)
            #Empty cell
            elif action == 0:
                #stack.clear()
                print(stack)
                return False
            #Case accepted
            elif action == -1:
                #stack.clear()
                print(stack)
                return True
