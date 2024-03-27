import csv
import sys

def push_program(stack):
    stack.append(".")
    stack.append("<statement_seq>")
    stack.append("<declarations>")
    stack.append("<fdecls>")
    return stack

def push_fdecls(stack):
    stack.append("<fdecls>")
    stack.append(";")
    stack.append("<fdec>")

    return stack

#REMEMBER WHEN APPENDING A PRODUCTION DO IT BACKWARDS
tokens = []
with open('output.txt', 'r') as file:
    for line in file:
        tokens.append(line.strip())
    tokens.append("END , $")
    
# process tokens
for i in range (len(tokens)):
    tokens[i] = tokens[i].strip()
    print(tokens[i])


position = 0
stack = []
token = tokens[position]
stack = push_program(stack)

while position < len(tokens):
    if stack[-1] == "<fdecls>":
        #first set
        print(tokens[position])
        if tokens[position] == "<def> ~ def":
            stack.pop()
            stack = push_fdecls(stack)
        elif tokens[position] == "<Identifier> ~ int" or tokens[position] == "<Identifier> ~ double": #follow set
            stack.pop()

    break

print("Phase 2 Complete")
#printing stack
print(stack)
print(len(tokens))
