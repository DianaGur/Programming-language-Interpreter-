# Programming-language-Interpreter-
This is a self-built programming language, which simulates a Python interpreter.

# INTRODUCTION: 
- The program's language is very similar to the Lisp PL. It supports simple math operations such as: 
addition, subtraction, multiplication, and division. 
- It can also manage 'while' loops and short 'If' statements.
- All these abilities allow us to solve complicated problems, using simple programs, via the computer.
- We chose our program to be dynamically typed, because those languages offer flexibility and simplicity, 
developers do not need to declare variable types explicitly, and they can work with a wide range of data types without restrictions. 

# MEMORY: 
- This PL uses a self-manageable memory. This means, that we don`t have to deal with memory allocation or leak. 
- In addition, there is a restriction on the length of the variable names, and the number of variables that can be used in one running program. 

# SYNTAX: 
There is a BNF file for our PL, that explains an acceptable input. 
Before using the language, please make sure you are familiar with the BNF file. 

# NOTICE: 
Every syntax error will cause a print message to the user, explaining why the error occurred. Both the if statement and while loop are allowed up to three levels.

# Problems & Solutions: 
1. Separating of the parts of condition/placement - 
We wanted to know how to split the parts of the conditions or placement. 
Solution: We Placed the sign of the expression in the middle. 
The sign separates the parts of the expression automatically.

2. Timing in printing results of logical expression/ math expression - we wanted to let the program print the result for those expressions.
Solution: We Added the function parameter from the boolean type to indicate the printing result.

3. Aborting while loop if the levels are more than 3 - 
when exiting the 4th loop the flow continued to enter it repeatedly.
Solution: variable in the memory class that indicates exiting all levels of while loops. 
