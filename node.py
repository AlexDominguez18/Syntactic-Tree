class Node(object):

    def __init__(self, number=0, token=''):
        self.number = number
        self.token = token
        self.lexeme = ''
        self.type = ''
        self.ambit = ''
        #Next Node
        self.next = None

    def set_next(self, next):
        self.next = next

    def get_number(self):
        return self.number

    def get_token(self):
        return self.token

    def get_lexeme(self):
        return self.lexeme
    
    def get_next(self):
        return self.next