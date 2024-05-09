# Programming-language-Interpreter-
This is a self build programming language using python interpreter.

INTRODUCTION: 
The program language is very similar to the Lisp PL. The program supports simple math opration such as: addition, subtraction, multiplication and division. 
Also the program can manage while loops and short "If" statments. All this allows you to create very simple programs that can solve complicated problems using 
computer. 
We choose the program to be dynamically typed because those languages offer flexibility and simplicity, as developers do not need to declare variable types explicitly, and they can work with a wide range of data types without restrictions. 

MEMORY: 
This PL is a self managable memory. this menas that you don`t have to deal with memory allocation or leack. In addition there are restriction in the
lenght of the veriable names, and the number of veribles that can be used in one program. 

SYNTAX: 
There is a BNF file of the program that explains an acceptable Before using the langauge please make sure you are familiare with the BNF file of the PL. 

NOTICE: 
Every syntax error will cause an print massage to the user explaining him why the error accuerd. The if statement or while loop allowed up to three levels.

Problems & Solutions: 
1. seperate the parts of condition/placemant - We wanted to know how to split the parts of the conditions or placement. 
solution: Place the sign of the expression in the middle. The sign seperates automatucaaly the parts of the expression.
2. Timing in printing result of logical expression/ math expression - we wnated to let the program to prunt th result fo those expressions.
solution: Add function permeater from boolean type to give an indication about printing result
3. Abort while loop if the levels are more than 3 - when exiting the 4th loop the flow continued to enter it again and again.
solution: variable in the memory class that gives indication to exit all levels of while loops. 

