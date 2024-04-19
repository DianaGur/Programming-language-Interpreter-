# Define the lexer to tokenize input Lisp code
def tokenize(code):
    return code.replace('(', ' ( ').replace(')', ' ) ').split()

# Define the parser to generate an Abstract Syntax Tree (AST)
def parse(tokens):
    if len(tokens) == 0:
        raise SyntaxError('Unexpected EOF while parsing')
    token = tokens.pop(0)
    if token == '(':
        ast = []
        while tokens[0] != ')':
            ast.append(parse(tokens))
        tokens.pop(0)  # pop off ')'
        return ast
    elif token == ')':
        raise SyntaxError('Unexpected )')
    else:
        return atom(token)

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
def evaluate(ast, env):
    if isinstance(ast, list):
        if ast[0] == 'defun':
            # Handle function definition
            _, func_name, params, body = ast
            env[func_name] = lambda *args: evaluate(body, {**env, **dict(zip(params, args))})
            return func_name
        else:
            # Handle function call
            func = evaluate(ast[0], env)
            args = [evaluate(arg, env) for arg in ast[1:]]
            return func(*args)
    elif isinstance(ast, str):
        # Look up variable in environment
        return env.get(ast, ast)
    else:
        # Return literals
        return ast

# Example usage
if __name__ == '__main__':
    # Sample Lisp code
    lisp_code = "(defun square (x) (* x x))"
    lisp_code += "(square 5)"

    # Tokenize and parse Lisp code
    tokens = tokenize(lisp_code)
    ast = parse(tokens)

    # Evaluate the AST
    global_env = {}
    result = evaluate(ast, global_env)
    print("Result:", result)  # Output: 25

