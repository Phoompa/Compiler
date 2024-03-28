import csv
import sys
#REMEMBER WHEN APPENDING A PRODUCTION DO IT BACKWARDS



def SyntaxAnalysis(VarSet, TerminalSet, tokens):
    iterations = 0
    position = 0
    startSymbol = "<program>"
    stack = []
    production = []
    stack.append(startSymbol)
    row = 0 #Represents row in LL1Table
    column = 0 #Represents column in LL1Table
 #Note: When pushing a terminal to the stack, do not use < > brackets
    while(len(stack) > 0):
        A = stack[-1] #symbol at the top of the stack
        print("Symbol at the top of the stack: " + A)
        r = tokens[position] #current token
        print("Current token: " + r)
        row = -1
        column = -1
        production.clear()
        
        if A in TerminalSet or A == "END~$":
            
            r = r.split('~')
            if A == 'letter': #for this case, check to see if R is an identifier
                if r[0] == '<Identifier>':
                    stack.pop()
                    print("Terminal successfully found and removed!")

                else:
                    print("Error, terminal letter is found but current token is not an <Identifier>")
            
            elif A == 'INTEGER':
                if r[0] == '<int>':
                    stack.pop()
                    print("Terminal successfully found and removed!")
                else:
                    print("Error, terminal INTEGER is found but current token is not an <int>")
                    
            elif A == 'DOUBLE':
                if r[0] == '<double>':
                    stack.pop()
                    print("Terminal successfully found and removed!")
                else:
                    print("Error, terminal DOUBLE found but current token is not an <int>")
            
            elif A == r[1] or r[1] == '$':
                stack.pop()
                print("Terminal successfully found and removed!")
            else:
                print("ERROR: Terminal found at the top of the stack, but current token does not match")
            position = position + 1
        
        elif A in VarSet:
            #get corresponding row number for A
            for i in range(len(LL1Table)):
                if A == LL1Table[i][0]: #row corresponding to production exists
                    row = i
                    
            if row == -1: #row corresponding to production does not exist.
                print("ERROR: Invalid Variable, not located in LL1 Table")
                #BREAK HERE FOR TESTING
                break
                
            #get corresponding column number for r
            
            #only ones that wont match up is: <Identifier>. <Identifier>~int and double match so handle this with an else after.
            for j in range(len(LL1Table[0])):

                if r == LL1Table[0][j]: # corresponding column exists in Table
                    column = j
            if column == -1:
                r = r.split('~')
                if r[0] == '<Identifier>':
                    column = 5
                    print("Successfully handled <Identifier>")
                    print(LL1Table[0][5])
                else:
                    print("ERROR: Invalid input token, not located in LL1 Table")
                    #BREAK HERE FOR TESTING
                    break
           
            #Now that you have the row and column, check to see if there is a production
            if LL1Table[row][column] != '': #production exists
                
                if LL1Table[row][column] == "epsilon": #current token is a follow set
                    stack.pop()
                
                else: #current token is a part of the first set
                    stack.pop()
                    production = LL1Table[row][column].split('~')
                    for i in production [::-1]: #iterates through elements backwards and pushes them onto the stack
                        if i == 'def ':
                            stack.append('def')
                        else:
                            if i != '':
                                stack.append(i)
                    
            else:
                print("Error, production for given row and column does not exist.")
                #BREAK HERE FOR TESTING
                break
                position = position + 1
             
        print("Iteration Complete! stack: ")
        print(stack)
        iterations = iterations + 1
        if iterations > 100 or position >= len(tokens):
            break 
        
    return stack

#Putting tokens into an array
tokens = []
with open('output.txt', 'r') as file:
    for line in file:
        tokens.append(line.strip())
    tokens.append("END~$")
    
# process tokens
for i in range (len(tokens)):
    tokens[i] = tokens[i].strip()
    

#process set of variables
with open('VariableSet.txt','r') as file:
    VarSet = file.read().splitlines()
        
for i in range(len(VarSet)):
    VarSet[i] = VarSet[i].strip()
    
#process set of terminals
with open('TerminalSet.txt','r') as file:
    TerminalSet = file.read().splitlines()
    
for i in range(len(TerminalSet)):
    TerminalSet[i] = TerminalSet[i].strip()
    
#Processing LL1 table into a 2D array
with open('CP471 -- LL(1) Table - Sheet1.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    LL1Table = []
    for row in csv_reader:
        LL1Table.append(row)
        
#Removing any whitespaces in LL1 table
for i in range(len(LL1Table)):
    for j in range(len(LL1Table[i])):
        LL1Table[i][j] = LL1Table[i][j].strip()

print("Phase 2 Complete")
#printing stack
print("---------- START OF PHASE 2 ----------")
stack = SyntaxAnalysis(VarSet, TerminalSet, tokens)
print("---------- PHASE 2 COMPLETE----------")


#print(stack)
#print("---------- SET OF VARIABLES ----------")
#print(VarSet)
#print("---------- SET OF TERMINALS ----------")
#print(TerminalSet)
#print("---------- LIST OF TOKENS ----------")
#print(tokens)
#print("---------- LL1 Table ----------")
#for i in range(len(LL1Table)):
#    for j in range(len(LL1Table[i])):
#        if LL1Table[i][j] is not '':
#            print(LL1Table[i][j])
#q = LL1Table[1][2].split('~')
#tempstack = []
#for i in q [::-1]:
#    tempstack.append(i)
#print(tempstack)
#print(len(LL1Table))