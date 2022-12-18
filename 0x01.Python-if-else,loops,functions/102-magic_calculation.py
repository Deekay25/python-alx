#information source
#https://www.tutorialspoint.com/disassembler-for-python-bytecode#:~:text=The%20dis%20module%20in%20Python,implementation%20detail%20of%20the%20interpreter.

#disassembler for python bytecode
#The dis module supports the analysis of CPython bytecode by disassembling it.

import dis
#dis() function
#The function dis() generates disassembled representation of any Python code source 
# i.e. module, class, method, function, or code object
def hello():
    print('hello world')

dis.dis(hello)

#Bytecode()
#This is the constructor. Analyse the bytecode corresponding 
# to a function, generator, method, 
# string of source code, or a code object. 
# This is a convenience wrapper around many of the functions
string = dis.Bytecode(hello)
for x in string:
    print(x)

#code_info()
#This function returns information of Python code object.
cinfo = dis.code_info(hello)
print(cinfo)

#show_code()
#This function prints detailed code information of Python module, function or class
scode = dis.show_code(hello)
print("starting", scode)

#disassemble()
#This function disassembles a code object and gives output divided in the following columns −
#the line number, for the first instruction of each line
#the current instruction, indicated as -->,
#a labelled instruction, indicated with >>,
#the address of the instruction,
#he operation code name,
#operation parameters, and
#nterpretation of the parameters in parentheses.
codeInString = 'a = 5\nb = 6\nsum = a + b \ nprint("sum = ",sum)'
codeObejct = compile(codeInString, 'sumstring', 'exec')
dis.disassemble(codeObejct)


#get_instructions()
#This function returns an iterator over the instructions in the supplied function, 
# method, source code string or code object. The iterator generates a series of Instruction 
# named tuples giving the details of each operation in the supplied code.

it=dis.get_instructions(code)
for i in it:
    print (i)


#alx challenge
#!/usr/bin/python3
#not done by me
def magic_calculation(a, b, c):
    if a < b:
        return c
    if c > b:
        return a + b
    return (a * b) - c