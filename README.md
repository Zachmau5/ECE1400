# ECE1400
python and c++ course
File I/O (hw04a.py):  Write a python program named "hw04a.py" that:
Accepts an input and output filename from the command line ./hw04a.py <input filename> <output filename = "out.txt">
If no input filename is provided, prompt the user to enter one
If no output filename is provided default to "out.txt"
Reads the input file line by line
Each line in the file will be in the format "<value>,<value>/n"
Store the values in variables and calculate their sum
Print a line to the screen and to the output file according to this format as floats with 2 decimal place precision
<value 1>+<value 2>=<sum>\n
Interactive I/O (hw04b.py):  Write a simple calculator that does + - * / on two numbers
  Your program should prompt the user with a "> " and then the user will type
<val1> <operator> <val2>\n
The program should accept any valid numbers with or without spaces separating them from the operators:
"-1.3e-4 + 5.6e-4"
"5/6"
If the numbers cannot be correctly read it must print "Invalid input\n" and continue
The <operator> must be one of  +-/*
If the operator is not +,-,/ or * it must print "Invalid operator\n" and continue
The program will print the result as
<val1> <operator> <val2> = <result>\n
use the "g" format specifier for the numbers
If the user types "quit" the program will exit
I will test it by streaming the file hw04b.input into it and it should produce an output matching hw04b.correct.
