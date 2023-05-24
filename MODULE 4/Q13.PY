# Explain Exception handling? What is an Error in Python? 
Exceptions are events that are used to modify the flow of control through a program when the error occurs. Exceptions get triggered automatically on finding errors in Python.

These exceptions are processed using five statements. These are:

try/except: catch the error and recover from exceptions hoist by programmers or Python itself.
try/finally: Whether exception occurs or not, it automatically performs the clean-up action.
assert: triggers an exception conditionally in the code.
raise: manually triggers an exception in the code.
with/as: implement context managers in older versions of Python such as - Python 2.6 & Python 3.0.
The last was an optional extension to Python 2.6 & Python 3.0.

ERROR :
Errors are the problems in a program due to which the program will stop the execution. On the other hand, exceptions are raised when some internal events occur which changes the normal flow of the program. 
Two types of Error occurs in python. 
 

1.Syntax errors

2.Logical errors (Exceptions) 

Syntax errors
When the proper syntax of the language is not followed then a syntax error is thrown.

logical errors(Exception)
When in the runtime an error that occurs after passing the syntax test is called exception or logical type. For example, when we
divide any number by zero then the ZeroDivisionError exception is raised, orwhen we import a module that does not exist then 
ImportError is raised.