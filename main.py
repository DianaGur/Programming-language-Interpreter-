
# Define the class memory of the program
class Prog_mem:
    def __init__(self):
        self.memory = {}        # var dictionary
        self.stack = []    # First cartridge that contains operators
        self.factors = []      # Second cartridge to operate math calculations
        self.t_operate = ('+', '-', '*', '/')
        self.t_logic = ('==', '>', '<')
        self.key_words = ('if', 'while', 'then')
        self.condition = False     # Track the nested conditions up to 3 levels
        self.track_if = 0
        self.loop = False           # Track the nested loops up to 3 levels
        self.track_loop = 0

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

    def naming_validation(self):
        pass


def is_valid(inpt):
     """
       This function classifies the expression that was given to her from the user.
       After the classification, the function sends the list to the processing functions
       in order to get the right output.
       :param inpt: List of strings that was made from the string input of the user
       :return: None.
       """
    if len(inpt) == 0:
        raise SyntaxError('Unexpected EOF while parsing')
    if len(inpt) >= 100:
        raise SyntaxError('Unsuitable length of the input, length should be less than 30 chars')
    counter = 0
    for char in inpt:
        if char == '(':
            counter = counter + 1
        if char == ')':
            counter = counter - 1

    if counter != 0:
        raise SyntaxError('uncompetitive number of brackets')


def tokenize(code):
    """
       This function classifies the expression that was given to her from the user.
       After the classification, the function sends the list to the processing functions
       in order to get the right output.
       :param inpt: List of strings that was made from the string input of the user
       :return: None.
       """
    return code.replace('(', '').replace(')', '').split()


# # Define the parser to generate an Abstract Syntax Tree (AST)
# def parse(tokens, mem):
#
#     if len(tokens) > 1:
#         mem.factors = tokens.copy()
#         # while len(tokens):
#         #     part = tokens.pop(0)
#         #     if part.isdigit():
#         #         mem.factors.append(int(part))
#         #     elif part != ')' and part != '(':
#         #         mem.operators.append(part)
#         return
#
#     token = tokens.pop(0)
#     return atom(token)


def logic_exp(exp_logic, c):

    """
    This function calculate from list the logic expression result.
    :param exp_logic: List of strings that represent condition
    :return: boolean
    """
    x = []
    y = []
    for i in range(len(exp_logic)):
        k = exp_logic.pop(0)
        if k == c:
            break
        x.append(k)

    y = exp_logic.copy()

    if len(x) > 1:
        part1 = int(classifier(x))
    else:
        part1 = x.pop(0)
        if part1.isdigit():
            part1 = int(part1)
        else:
            part1 = memory.search(part1)

    # part 1 is None?
    if len(y) > 1:
        part2 = int(classifier(y))
    else:
        part2 = y.pop(0)
        if part2.isdigit():
            part2 = int(part2)
        else:
            part2 = memory.search(part2)

    if c == '>':
        print(part1 > part2)
        return part1 > part2
    elif c == '<':
        print(part1 < part2)
        return part1 < part2
    elif c == '==':
        print(part1 == part2)
        return part1 == part2

    return False


def calc_result(inpt):
    """
    This function is capable of dealing with math expressions of the new programming langauge.
    It can handle all the types of math expressions with prefix operators.
    :param inpt: List of string after splitting the input of the user.
    :return: The number of the solved equation
    """
    while len(inpt) > 1:
        index = 0
        operation = ''
        for i in range(len(inpt) - 1, -1, -1):    # Search for the first operator for the end fo the list
            index = index - 1
            if memory.find_oper(inpt[i]):
                operation = inpt[i]
                break
        if inpt[index + 1].isdigit():           # get first number ofter the operator
            x = int(inpt[index + 1])
        else:
            x = int(memory.search(inpt[index + 1]))

        if inpt[index + 2].isdigit():           # get second number ofter the operator
            y = int(inpt[index + 2])
        else:
            y = int(memory.search(inpt[index + 2]))

        if operation == '+':
            x = x + y
        elif operation == '-':
            x = x - y
        elif operation == '*':
            x = x * y
        elif operation == '/':
            x = x / y

        inpt.pop(index + 2)
        inpt.pop(index + 2)
        inpt.pop(index + 2)
        inpt.append(str(int(x)))    # Dealing with float numbers by converting them to int and then to string
    return inpt.pop(0)


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
def classifier(inpt):

    """
    This function classifies the expression that was given to her from the user.
    After the classification, the function sends the list to the processing functions
    in order to get the right output.
    :param inpt: List of strings that was made from the string input of the user
    :return: None.
    """

    if inpt[0] == 'if':
        inpt.pop(0)     # Removes 'if' from the input list
        if_handler(inpt)

    elif inpt[0] == 'while':
        inpt.pop(0)     # Removes 'while' from the input list
        while_handler(inpt)

    else:
        if inpt[0] == '=':
            pass
        else:
            res = (calc_result(inpt))
            return res


def if_handler(expression):

    """
       This function classifies the expression that was given to her from the user.
       After the classification, the function sends the list to the processing functions
       in order to get the right output.
       :param inpt: List of strings that was made from the string input of the user
       :return: None.
       """

    condition = []
    c = ' '
    for i in range(len(expression)):
        part = expression.pop(0)
        if part == 'then':
            break
        elif memory.find_logic(part):
            c = part
            condition.append(part)
        else:
            condition.append(part)
    print(condition)
    body = expression.copy()
    print(body)
    if logic_exp(condition, c):
        classifier(body)
    else:
        return print("-")   # indication hasnt enter the if


def while_handler(inpt):

    """
       This function classifies the expression that was given to her from the user.
       After the classification, the function sends the list to the processing functions
       in order to get the right output.
       :param inpt: List of strings that was made from the string input of the user
       :return: None.
       """

    condition = []
    c = ' '
    for part in inpt:
        if part == ':':
            break
        elif memory.find_logic(part):
            c = part
            condition.append(part)
        else:
            condition.append(part)
        inpt.pop(0)
    print(condition)
    body = inpt.copy()
    inpt.clear()
    while logic_exp(condition, c):
        classifier(body)
    return print("end")     # indication for finishing the


#if __name__ == '__main__':

memory = Prog_mem()   # consider to make an global var
while True:
    str_inpt = input(">>>")
    print(str_inpt)

    if str_inpt == 'close':      # Ends the program
        break
        # Sample Lisp code
        #need to be added
    is_valid(str_inpt)
        # Tokenize and parse the code
    code_inpt = tokenize(str_inpt)
    classifier(code_inpt)
        #code_inpt = tokenize(str_inpt)
        #print(code_inpt)
        # parse(code_inpt, mem)
        #classifier(code_inpt)
