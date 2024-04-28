# Define the class memory of the program
class Prog_mem:
    def __init__(self):
        self.memory = {}        # var dictionary 
        self.logic_oper = []    # First cartridge that contains operators
        self.factors = []      # Second cartridge to operate math calculations
        self.t_operate = ('+', '-', '*', '/')
        self.t_logic = ('=', '>', '<')

    def search(self, variable):
        for var in self.memory.keys():
            if var == variable:
                return self.memory.get(var)

    def insert_var(self, variable, value):

        if len(self.memory.keys()) >= 10:
            return print("Maximum amount of variables has been reached")
        for letter in self.memory.keys():
            if letter == variable:
                self.memory.pop(letter)

        self.memory.update({variable: value})      #inserts the new variable in the dictionary

    def find_oper(self, operator):
        for c in self.t_operate:
            if c == operator:
                return True

        return False

    def find_logic(self, symbol):
        for c in self.t_logic:
            if c == symbol:
                return True

        return False


def is_valid(inpt):
    if len(inpt) == 0:
        raise SyntaxError('Unexpected EOF while parsing')
    if len(inpt) >= 30:
        raise SyntaxError('Unsuitable length of the input, length should be less than 30 chars')
    pass


def tokenize(code):
    return code.replace('(', '').replace(')', '').split()


# Define the parser to generate an Abstract Syntax Tree (AST)
def parse(tokens, mem):

    if len(tokens) > 1:
        mem.factors = tokens.copy()
        # while len(tokens):
        #     part = tokens.pop(0)
        #     if part.isdigit():
        #         mem.factors.append(int(part))
        #     elif part != ')' and part != '(':
        #         mem.operators.append(part)
        return

    token = tokens.pop(0)
    return atom(token)


def Logic_exp(mem):
'''
function designr
''' 
    c = mem.logic_oper.pop(0)
    x = mem.logic_oper.pop(0)
    if x.isdigit():
        x = int(x)
    else:
        x = mem.search(x)
    y = mem.logic_oper.pop(0)
    if y.isdigit():
        y = int(x)
    else:
        y = mem.search(x)

    if c == '>':
        return x > y
    elif c == '<':
        return x < y
    elif c == '==':
        return x == y

    return False


def calc_result(mem):
'''
math solver function
'''
    while len(mem.factors) > 1:
        index = 0
        c = ''
        for i in range(len(mem.factors) - 1, -1, -1):
            index = index - 1
            if mem.find_oper(mem.factors[i]):
                c = mem.factors[i]
                break
        if mem.factors[index + 2].isdigit():
            x = int(mem.factors.pop(index+2))
        else:
            x = int(mem.search(mem.factors[index + 2]))
            mem.factors.pop(index + 2)
        if mem.factors[index + 2].isdigit():
            y = int(mem.factors.pop(index + 2))
        else:
            y = int(mem.search(mem.factors[index + 2]))
            mem.factors.pop(index + 2)

        mem.factors.pop(index+2)

        if c == '+':
            x = x + y
        elif c == '-':
            x = x - y
        elif c == '*':
            x = x * y
        elif c == '/':
            x = x / y

        mem.factors.append(x)
    res = mem.factors.pop(0)
    return res


# Helper function to convert tokens to appropriate data types
def atom(token):
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return token


# Define the evaluator to execute Lisp expressions
def classifier(input):   #( change ast to input )
    if input [0] == 'if':
        ast.pop(0)     # Removes 'if' from the input list
        condition = []
        # Handle if statement definition
        for i in range(len(ast)):
            part = ast.pop(0)
            if part == 'then':
                break
            else:
                condition.append(part)
        print(condition)
        body = ast.copy()
        ast.clear()
        print(body)
        if_handler(condition, body)
    elif ast[0] == 'while':
        condition = []
        ast.pop(0)
        for part in ast:
            if part == 'then':
                break
            else:
                condition.append(part)
            ast.pop(0)
        print(condition)
        body = ast.copy()
        ast.clear()
        while_handler(condition, body)
    else:
        if mem.find_logic(ast[0]):   
            pass
        elif ast[0] == '=':   
            pass
        else:
             print(calc_result(mem)) 



def if_handler(condition, body):
    if Logic_exp(condition):
        classifier(body)
    else:
        return print("-")   # indication hasnt enter the if


def while_handler(condition, body):
    while Logic_exp(condition):
        classifier(body)
    return print("end")     # indication for finishing the


# Example usage
if __name__ == '__main__':

    mem = Prog_mem()
    while True:
        str_inpt = input(">>>")
        print(str_inpt)
        # Sample Lisp code
        #need to be added

        # Tokenize and parse the code
        code_inpt = tokenize(str_inpt)
        print(code_inpt)
        # parse(code_inpt, mem)
        classifier(code_inpt)
        result = calc_result(mem)

        # Evaluate the AST
        # global_env = {}
        # result = evaluate(ast, global_env)


