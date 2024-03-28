import csv
import sys
BUFFER_SIZE = 1024
START = 0

def csv_to_2Darray(file_path): #function to convert the transition table .csv file into a 2D array
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        temp_2Darray = []
        for row in csv_reader:
            temp_2Darray.append(row)
    
    return temp_2Darray

def keywords_to_list(file_path): #function to convert keywords.txt into a list containing all keywords
    with open(file_path,'r') as file:
        temp_array = file.read().splitlines()
    return temp_array

def final_states_to_list(file_path): #function to convert finalStates.txt into a list containing all final states
    with open(file_path,'r') as file:
        temp_array = [int(line.strip()) for line in file.readlines()]

    return temp_array
 
def getToken(state,file,IdentifierString): #function used to obtain token given a state

    if (state == 2): #Recognizes operator <=
        file.write("<Operator>~<=")
    
    elif (state == 3): #Recognizes operator <>
        file.write("<Operator>~<>")
        
    elif (state == 4): #Recognizes operator <
        file.write("<Operator>~<")
        
    elif (state == 6): #Recognizes operator ==
        file.write("<Operator>~==")
    
    elif (state == 7): #Recognizes operator =
        file.write("<Operator>~=")
        
    elif (state == 9): #Recognizes operator >=
        file.write("<Operator>~>=")
    
    elif (state == 10): #Recognizes operator >
        file.write("<Operator>~>")
        
    elif (state == 11): #Recognizes operator +
        file.write("<Operator>~+")
        
    elif (state == 12): #Recognizes operator -
        file.write("<Operator>~-")
        
    elif (state == 13): #Recognizes operator *
        file.write("<Operator>~*")
    
    elif (state == 14): #Recognizes operator /
        file.write("<Operator>~/")
    
    elif (state == 15): #Recognizes operator %
        file.write("<Operator>~%")
    
    elif (state == 16): #Recognizes operator ,
        file.write("<Operator>~,")
    
    elif (state == 17): #Recognizes operator ;
        file.write("<Operator>~;")
        
    elif (state == 18): #Recognizes operator (
        file.write("<Operator>~(")
        
    elif (state == 19): #Recognizes operator )
        file.write("<Operator>~)")        
        
    elif (state == 21): #Recognizes Identifiers
        file.write("<Identifier>~" + IdentifierString)

    elif(state == 25): #Recognizes keyword and
        file.write("<and>~and")
    
    elif(state == 29): #Recognizes keyword def
        file.write("<def>~def")
    
    elif(state == 31): #Recognizes keyword do
        file.write("<do>~do")

    elif (state == 36): #Recognizes keyword else
        file.write("<else>~else")
    
    elif (state == 40): #Recognizes keyword fed
        file.write("<fed>~fed")
    
    elif (state == 42): #Recognizes keyword fi
        file.write("<fi>~fi")

    elif (state == 45): #Recognizes keyword if
        file.write("<if>~if")
    
    elif (state == 48): #Recognizes keyword od
        file.write("<od>~od")

    elif (state == 50): #Recognizes keyword or
        file.write("<or>~or")
    
    elif (state == 54): #Recognizes keyword not
        file.write("<not>~not")

    elif (state == 60): #Recognizes keyword print
        file.write("<print>~print")

    elif (state == 67): #Recognizes keyword return
        file.write("<return>~return")
    
    elif (state == 72): #Recognizes keyword then
        file.write("<then>~then")

    elif (state == 78): #Recognizes keyword while
        file.write("<while>~while")

    elif (state == 80): #Recognizes int
        file.write("<int>~int")
    
    elif (state == 83): #Recognizes double
        file.write("<double>~double")
        
    elif (state == 84) : #Recognizes [
        file.write("<Operator>~[")
        
    elif (state == 85) : #Recognizes ] 
        file.write("<Operator>~]")
    file.write("\n")


def lexical_analysis(transition_table, keywords, final_states, decrement_final_states, file_name):
    output_file = open('output.txt','w')
    error_file = open('errors.txt', 'w')
    with open(file_name, 'r') as file:
        buffer1 = file.read(BUFFER_SIZE)
        buffer2 = file.read(BUFFER_SIZE)
        #print("Length of Buffer1")
        #print(len(buffer1))
        #print("Length of Buffer2")
        #print(len(buffer2))
        IdentifierStringbuffer = 0
        IdentifierString = "" #used to store Identifier string value along with token
        first = 0
        while buffer1:
            current = transition_table[0][START]    #current state
            i = 0
            line_count = 1
            while i < len(buffer1):   #iterates through every char in buffer
                # Process character in buffer1
                #print(buffer1[i])
                previous = current
                current = int(transition_table[int(ord(buffer1[i]) - 1)][int(current)])
                if first == 0 and current != 20:
                    if (65 <= ord(buffer1[i]) <= 90) or (97 <= ord(buffer1[i]) <= 122):
                        first = 1
                        IdentifierString = IdentifierString + buffer1[i]
                    
                #print(current)
                if current == 20:
                    if IdentifierStringbuffer == 0: 
                        if (65 <= ord(buffer1[i-1]) <= 90) or (97 <= ord(buffer1[i-1]) <= 122):
                            #IdentifierString = IdentifierString + buffer1[i-1]
                            #IdentifierStringbuffer = 1
                            print("")
                    IdentifierString = IdentifierString + buffer1[i]


                if current in final_states: #Final state reached
                    #print("final state reached: ")
                    getToken(current,output_file,IdentifierString)
                    print(IdentifierString)
                    IdentifierString = '' #reset identifier String
                    IdentifierStringbuffer = 0
                    first = 0

                    if current in decrement_final_states: #decrement one char back
                        #print("FINAL STATE REACHED")
                        #print(buffer1[i])
                        i = i - 1

                    
                    current = transition_table[0][START]
                elif current == -1: #Error
                    #print("ERROR")
                    error_file.write("Char: " +  buffer1[i] + " line #: " + str(line_count))
                    current = transition_table[0][START]

                if (ord(buffer1[i]) == 10): # /n encountered
                    line_count += 1


                i+= 1
                
            

            

            buffer1 = buffer2
            #print("-------------------------------------------BUFFER SWITCH-------------------------------------------")
            buffer2 = file.read(BUFFER_SIZE)
        output_file.close()
        error_file.close()

#ALL OF THE FUNCTIONS ABOVE THIS LINE ARE PART OF PHASE 1





def parse_program(tokens, position): # <program>
    print("successfully entered parse_program")

    
    token = updateToken(tokens, position)
    position = parse_fdecls(tokens, position)
    token = updateToken(tokens, position)
    position = parse_declarations(tokens, position)
    token = updateToken(tokens, position)
    position = parse_statement_seq(tokens, position)
    token = updateToken(tokens, position)


    if token[1].strip() == '$':
        print("Reached the end, parsing successful")
    return position

def parse_declarations(tokens,position):
    print("successfully entered parse_declarations")
    lookahead_token = tokens[position + 1].split(',')
    token = tokens[position].split(',')
    token = checkComma(token)
    lookahead_token = checkComma(lookahead_token)
    #sys.exit()

    print(token)

    if lookahead_token[0].strip() == '<while>' or lookahead_token[0].strip() == '<if>' or lookahead_token[0].strip() == '<print>' or lookahead_token[0].strip() == '<return>' or lookahead_token[0].strip() == '<Identifier>' : #follow set
        print(lookahead_token)
        return position
    else:
        
        if token[0].strip() == '<Identifier>':
            sys.exit()
            if token[1].strip() == 'int' or token[1].strip() == 'double' or token[1].strip() == 'duble':
                #position = parse_decl(tokens, position)
            

                if token[1].strip() == ';':
                    position = position + 1
                    token = updateToken(tokens, position)

                    print("Parse successful: ; recognized")
                    
                position = parse_declarations_prime(tokens, position)
                token = updateToken(tokens, position)

        else:
            print("Parsing error at <declarations> --> <decl>; <declarations> ")
    
    return position

def parse_declarations_prime(tokens,position):
    print("successfully entered parse_declarations_prime")
    lookahead_token = tokens[position + 1].split(',')
    token = tokens[position].split(',')
    token = checkComma(token)
    lookahead_token = checkComma(lookahead_token)

    if lookahead_token[0].strip() == '<while>' or lookahead_token[0].strip() == '<if>' or lookahead_token[0].strip() == '<print>' or lookahead_token[0].strip() == '<return>' or lookahead_token[0].strip() == '<Identifier>' : #follow set
        return position
    else:
        if token[0].strip() == '<Identifier>':
            if token[1].strip() == 'int' or token[1].strip() == 'double' or token[1].strip() == 'duble':
                position = parse_decl(tokens, position)
                token = updateToken(tokens, position)

                if token[1].strip() == ';':
                    position = position + 1
                    token = updateToken(tokens, position)

                    print("Parse successful: ; recognized")
                    
                    
                position = parse_declarations_prime(tokens, position)
                token = updateToken(tokens, position)

        else:
            print("Parsing error at <declarations'> --> <decl>; <declarations'> ")
    
    return position

def parse_decl(tokens, position):
    print("successfully entered parse_decl")
    token = tokens[position].split(',')
    token = checkComma(token)
    if token[0].strip() == '<Identifier>':
        if token[1].strip() == 'int' or token[1].strip() == 'double' or token[1].strip() == 'duble':
            position = parse_type(tokens,position)
            token = updateToken(tokens, position)
            position = parse_varlist(tokens, position)
            token = updateToken(tokens, position)


    return position

def parse_varlist(tokens, position):
    print("successfully entered parse_varlist")
    token = tokens[position].split(',')
    
    token = checkComma(token)

    if token[0].strip() == '<Identifier>':
        position = parse_var(tokens, position)
        token = updateToken(tokens, position)

        position = parse_varlist_prime(tokens,position)
        token = updateToken(tokens, position)

    return position

def parse_varlist_prime(tokens, position):
    print("successfully entered parse_varlist_prime")
    lookahead_token = tokens[position + 1].split(',')
    token = tokens[position].split(',')
    token = checkComma(token)
    lookahead_token = checkComma(lookahead_token)
        
    if lookahead_token[1].strip() == ';': #follow set
        return position
    else: #first set
        if token[1].strip() == ',':
            print("Parse successful: , recognized")
            position = position + 1
            token = tokens[position].split(',')
            token = checkComma(token)
        else:
            print("Error at <varlist'>")
        position = parse_varlist(tokens, position)
        token = updateToken(tokens, position)


    return position

def parse_statement_seq(tokens,position):
    print("successfully entered parse_statement_seq")
    token = tokens[position].split(',')
    token = checkComma(token)
    sys.exit()
  
    if token[0].strip() == '<if>' or token[0].strip() == '<Identifier>' or token[0].strip() == '<while>'  or token[0].strip() == '<print>' or token[0].strip() == '<return>' or token[1].strip() == ';':
        position = parse_statement(tokens, position)
        token = updateToken(tokens, position)

        position = parse_statement_seq_prime(tokens, position)
        token = updateToken(tokens, position)

    return position

def parse_statement_seq_prime(tokens, position):
    print("successfully entered parse_statement_seq_prime")
    lookahead_token = tokens[position + 1].split(',')
    token = tokens[position].split(',')
    token = checkComma(token)
    lookahead_token = checkComma(lookahead_token)
        
    if lookahead_token[0].strip() == '<fi>' or lookahead_token[0].strip() == '<else>' or lookahead_token[0].strip() == '<od>' or lookahead_token[0].strip() == '<fed>' or lookahead_token[1].strip() == '$':#follow set
        return position
    else: # first set
        if token[1].strip() == ';':
            print("Parse successful: ; recognized")
            position = position + 1
            token = tokens[position].split(',')
            token = checkComma(token)
        else:
            print("Parse error at: <statement_seq'>")
        position = parse_statement_seq(tokens, position)
        token = updateToken(tokens, position)


    return position

def parse_statement(tokens, position):
    print("successfully entered parse_statement")
    lookahead_token = tokens[position + 1].split(',')
    token = tokens[position].split(',')
    token = checkComma(token)
    lookahead_token = checkComma(lookahead_token)
        
    if lookahead_token[1].strip() == ';':#follow set
        return position
    #elif below for: if <bexpr> then <statement_seq><statement'>
    elif token[0].strip() == '<if>':
        print("Parse successful: if recognized")
        position = position + 1
        token = tokens[position].split(',')
        token = checkComma(token)
        position = parse_bexpr(tokens, position)
        token = updateToken(tokens, position)

        if token[0].strip() == '<then>':
            print("Parse successful: <then> recognized")
            position = position + 1
            token = tokens[position].split(',')
            token = checkComma(token)
        else:
            print("Parse error: <statement>")
        position = parse_statement_seq(tokens, position)
        token = updateToken(tokens, position)

        position = parse_statement_prime(tokens, position)
        token = updateToken(tokens, position)


    #elif below for: <var> = <expr>
    elif token[0].strip() == '<Identifier>':
        position = parse_var(tokens,position)
        token = updateToken(tokens, position)

        if token[1].strip() == '=':
            print("Parse successful: = recognized")
            position = position + 1
            token = tokens[position].split(',')
            token = checkComma(token)

        else:
            print("Parse error at <statement>")
        position = parse_expr(tokens, position)
        token = updateToken(tokens, position)


    #elif below for: While <bexpr> do <statement_seq> od
    elif token[0].strip() == '<while>':
        print("Parse successful: while recognized")
        position = position + 1
        token = tokens[position].split(',')
        token = checkComma(token)
        position = parse_bexpr(tokens, position)
        token = updateToken(tokens, position)

        if token[0].strip() == '<do>':
            print("Parse successful: do recognized")
            position = position + 1
            token = tokens[position].split(',')
            token = checkComma(token)
        else:
            print("Parse error at <statement>")
        position = parse_statement_seq(tokens, position)
        token = updateToken(tokens, position)

        if token[0].strip() == '<od>':
            print("Parse successful: od recognized")
            position = position + 1
            token = tokens[position].split(',')
            token = checkComma(token)
        else:
            print("Parse error at <statement>")
    #elif for: print <expr>
    elif token[0].strip() == '<print>':
        print("Parse successful: print recognized")
        position = position + 1
        token = tokens[position].split(',')
        token = checkComma(token)
        position = parse_expr(tokens, position)
        token = updateToken(tokens, position)

    #elif for: Return <expr> 
    elif token[0].strip() == '<return>':
        print("Parse successful: return recognized")
        position = position + 1
        token = tokens[position].split(',') 
        token = checkComma(token)
        position = parse_expr(tokens, position)     
        token = updateToken(tokens, position)
 
    return position

def parse_bexpr(tokens, position):
    print("successfully entered parse_bexpr")
    token = tokens[position].split(',')
    token = checkComma(token)
    

    if token[1].strip() == '(' or token[0].strip() == '<not>':
        position = parse_bterm(tokens, position)
        token = updateToken(tokens, position)

        position = parse_bexpr_prime(tokens, position)
        token = updateToken(tokens, position)

    else:
        print("Parse error at <bexpr>")
    return position

def parse_bexpr_prime(tokens, position):
    print("successfully entered parse_bexpr_prime")
    lookahead_token = tokens[position + 1].split(',')
    token = tokens[position].split(',')
    token = checkComma(token)
    lookahead_token = checkComma(lookahead_token)
        
    if lookahead_token[1].strip() == ')' or lookahead_token[0].strip() == '<then>' or lookahead_token[0].strip() == '<do>':#follow set
        return position
    
    else: #first set
        if token[0].strip() == '<or>':
            print("Parse successful: or recognized")
            position = position + 1
            token = tokens[position].split(',')
            token = checkComma(token)
        else:
            print("Parse error at <bexpr'>")
            position = parse_bterm(tokens, position)
            token = updateToken(tokens, position)

            position = parse_bexpr_prime(tokens,position)
            token = updateToken(tokens, position)


    return position

def parse_bterm(tokens, position):
    print("successfully entered parse_bterm")
    token = tokens[position].split(',')
    
    token = checkComma(token)
       
    
    if token[1].strip() == '(' or token[0].strip() == '<not>':
        position = parse_bfactor(tokens, position)
        token = updateToken(tokens, position)

        position = parse_bterm_prime(tokens, position)
        token = updateToken(tokens, position)

    else:
        print("Parse error at <bterm>")
    return position

def parse_bterm_prime(tokens, position):
    print("successfully entered parse_bterm_prime")
    lookahead_token = tokens[position + 1].split(',')
    token = tokens[position].split(',')
    token = checkComma(token)
    lookahead_token = checkComma(lookahead_token)

    if lookahead_token[0].strip() == '<or>':#follow set
        return position
    
    else: #first set
        if token[0].strip() == '<and>':
            print("Parse successful: and recognized")
            position = position + 1
            token = tokens[position].split(',')
            token = checkComma(token)
        else:
            print("Parse error at <bterm'>")
        
        position = parse_bfactor(tokens, position)
        token = updateToken(tokens, position)

        position = parse_bterm_prime(tokens, position)

    return position

def parse_bfactor(tokens, position):
    print("successfully entered parse_bfactor")
    token = tokens[position].split(',')
    token = checkComma(token)
    if token[1].strip() == '(':
        print("Parse successful: ( recognized")
        position = parse_bexpr(tokens, position)
        token = updateToken(tokens, position)

        if token[1].strip() == ')':
            print("Parse successful: ) recognized")
            position = position + 1
            token = tokens[position].split(',')
            token = checkComma(token)
        else:
            print("Parse error at <bfactor>")
    elif token[1].strip() == '(':
        print("Parse successful: ( recognized")
        position = position + 1
        token = tokens[position].split(',')
        token = checkComma(token)
        position = parse_expr(tokens, position)
        token = updateToken(tokens, position)
        position = parse_comp(tokens, position)
        token = updateToken(tokens, position)
        position = parse_expr(tokens, position)
        token = updateToken(tokens, position)

        if token[1].strip() == ')':
            print("Parse successful: ) recognized")
            position = position + 1
            token = tokens[position].split(',')
            token = checkComma(token)
        else:
            print("Parse error at <bfactor>")

    elif token[0].strip() == '<not>':
        print("Parse successful: not recognized")
        position = position + 1
        token = tokens[position].split(',')
        token = checkComma(token)
        position = parse_bfactor(tokens, position)
        token = updateToken(tokens, position)

    else:
        print("Parse error at <bfactor>")
    return position

def parse_comp(tokens, position):
    print("successfully entered parse_comp")
    token = tokens[position].split(',')
    
    token = checkComma(token)
    if token[1].strip() == '<':
        print("Parse successful: < recognized")
        position = position + 1
        token = tokens[position].split(',')
        token = checkComma(token)
    elif token[1].strip() == '>':
        print("Parse successful: > recognized")
        position = position + 1
        token = tokens[position].split(',')
        token = checkComma(token)
    elif token[1].strip() == '==':
        print("Parse successful: == recognized")
        position = position + 1
        token = tokens[position].split(',')
        token = checkComma(token)
    elif token[1].strip() == '<=':
        print("Parse successful: <= recognized")
        position = position + 1
        token = tokens[position].split(',')
        token = checkComma(token)
    elif token[1].strip() == '>=':
        print("Parse successful: >= recognized")
        position = position + 1
        token = tokens[position].split(',')
        token = checkComma(token)
    elif token[1].strip() == '<>':
        print("Parse successful: <> recognized")
        position = position + 1
        token = tokens[position].split(',')
        token = checkComma(token)
    else:
        print("Parse error at <comp>")


    return position

def parse_statement_prime(tokens, position):
    print("successfully entered parse_statement_prime")
    token = tokens[position].split(',')
    
    token = checkComma(token)
    lookahead_token = checkComma(lookahead_token)
       
    

    if token[0].strip() == '<fi>':
        print("Parse successful: fi recognized")
        position = position + 1
        token = tokens[position].split(',')
        token = checkComma(token)
    elif token[0].strip() == '<else>':
        print("Parse successful: else recognized")
        position = position + 1
        token = tokens[position].split(',')
        token = checkComma(token)
        position = parse_statement_seq(tokens, position)
        token = updateToken(tokens, position)

        if token[0].strip() == '<fi>':
            print("Parse successful: fi recognized")
            position = position + 1
            token = tokens[position].split(',')
            token = checkComma(token)
        else:
            print("Parse error at <statement'>")
    else:
        print("Parse error at <statement'>")
    return position

def parse_fdecls(tokens, position):
    print("successfully entered parse_fdecls")
    token = tokens[position].split(',')
    token = checkComma(token)
   
    print(position)
    print(token[0])
    print(token[1])
    print(type(token[0]))
    if token[0].strip() == '<def>':

        position = parse_fdec(tokens, position)
        token = updateToken(tokens, position)
  
    if token[1].strip() == ';':
        position = position + 1
        token = tokens[position].split(',')
        token = checkComma(token)
        print("Parse successful, ; recognized")
    else:
        print("Parsing error at: <fdecls> -> <fdec>;<fdecls'>")
    position = parse_fdecls_prime(tokens, position)
    token = updateToken(tokens, position)

        
    return position

def parse_fdec(tokens, position):
    print("successfully entered parse_fdec")
    print("Entered Fdec")
    position = position + 1 #at this point def is terminal and to be here, current token needed to be def
    
    token = tokens[position].split(',')
    
    token = checkComma(token)
    
    
    if token[0].strip() == '<identifier>': #Parse <type>
        position = parse_type(tokens,position) 
        token = updateToken(tokens, position)


    
    
    if token[0].strip() == '<identifier>': #Parse <id>
        position = parse_fname(tokens, position)
        token = updateToken(tokens, position)

   
    
    if token[0].strip() == '<Operator>':
        if token[1].strip() == '(':
            position = position + 1 #terminal reached
            token = tokens[position].split(',')
            token = checkComma(token)
            
  
    if token[0].strip() == 'identifier': #parse params
        position = parse_params(tokens, position)
        token = updateToken(tokens, position)

 
    
   
    if token[0].strip() == '<Operator>':
        if token[1].strip() == ')':
            position = position + 1 #terminal reached
            token = tokens[position].split(',')
            token = checkComma(token)
            
    
    if token[0].strip() == '<Identifier>': #parse declarations
        position = parse_declarations(tokens, position)
        token = updateToken(tokens, position)

    print(token[1])
    if token[0].strip() == '<Identifier>' or token[0].strip() == '<if>' or token[0].strip() == '<while>' or token[0].strip() == '<print>' or token[0].strip() == 'return' or token[1].strip() == ';':
        position = parse_statement_seq(tokens,position)
        token = updateToken(tokens, position)


    
    
    if token[0].strip() == '<Fed>':
        position = position + 1 #terminal reached
        token = tokens[position].split(',')
        token = checkComma(token)

    return position

def parse_type(tokens, position):
    print("successfully entered parse_type")
    if token[1].strip() == "int":
        print("Parse successful, int identifier recognized")
    if token[1].strip() == "double" or token[1].strip() == "duble":
        print("Parse successful, int recognized")
    position = position + 1
    token = tokens[position].split(',')
    token = checkComma(token)

    
    
    return position

def parse_params(tokens, position):
    print("successfully entered parse_params")
    token = tokens[position].split(',')
    lookahead_token = tokens[position + 1].split(',')
    token = checkComma(token)
    lookahead_token = checkComma(lookahead_token)
        
    if lookahead_token[0].strip() == '<Operator>' and lookahead_token[1].strip() == ')': #follow set
        return position
    else: #first set
        if token[0].strip() == '<Identifier>':
            if token[1].strip() == 'int' or token[1].strip() == 'double' or token[1].strip() == 'duble':
                position = parse_type(tokens, position)
                token = updateToken(tokens, position)
                position = parse_var(tokens, position)
                token = updateToken(tokens, position)
                position = parse_params_prime(tokens, position)
                token = updateToken(tokens, position)

    return position

def parse_var(tokens, position):
    print("successfully entered parse_var")
    token = tokens[position].split(',')
    token = checkComma(token)
    
    if token[0].strip() == '<Identifier>':
        position = parse_id(tokens, position)
        token = updateToken(tokens, position)
        position = parse_var_prime(tokens, position)
        token = updateToken(tokens, position)

    else:
        print("Parsing Error at <var>")
    return position

def parse_var_prime(tokens, position):
    print("successfully entered parse_var_prime")
    token = tokens[position].split(',')
    lookahead_token = tokens[position + 1].split(',')
    token = checkComma(token)
    lookahead_token = checkComma(lookahead_token)
        
    if lookahead_token[1].strip() == '=' or lookahead_token[1].strip() == ',' or lookahead_token[1].strip() == '*' or lookahead_token[1].strip() == '/' or lookahead_token[1].strip() == '%': #follow set
        return position
    else:
        if token[0].strip() == '<Operator>' and token[1].strip() == '[':
            print("Parse successful, [] recognized")
            position = position + 1
            token = tokens[position].split(',')
            token = checkComma(token)
        position = parse_expr(tokens, position)
        token = updateToken(tokens, position)

        if token[0].strip() == '<Operator>' and token[1].strip() == ']':
            print("Parse successful, [] recognized")
            position = position + 1
            token = tokens[position].split(',')   
            token = checkComma(token)

    return position

def parse_expr(tokens, position):
    print("successfully entered parse_expr")
    token = tokens[position].split(',')
    token = checkComma(token)
   
    if token[0].strip() == "<Identifier>" or token[0].strip() == "<Int>" or token[0].strip() == "<Double>" or token[1].strip() == '(':
        position = parse_term(tokens, position)
        token = updateToken(tokens, position)
        position = parse_expr_prime(tokens, position)
        token = updateToken(tokens, position)

        print("")
    return position

def parse_expr_prime(tokens, position):
    print("successfully entered parse_expr_prime")
    token = tokens[position].split(',')
    lookahead_token = tokens[position + 1].split(',')
    token = checkComma(token)
    lookahead_token = checkComma(lookahead_token)
    print(f"Token at <expr'>: {token[0]} , {token[1]}")
    print(f"Lookahead_token at <expr>: {lookahead_token}")
    #follow set
    if lookahead_token[1].strip() == ']' or lookahead_token[1].strip() == '<' or lookahead_token[1].strip() == '>' or lookahead_token[1].strip() == '==' or lookahead_token[1].strip() == '<=' or lookahead_token[1].strip() == '>=' or lookahead_token[1].strip() == '<>' or lookahead_token[1].strip() ==  ')' or lookahead_token[1].strip() == ',' or lookahead_token[1].strip() == ';':
        print("RETURNNNNN")
        return position
    else:
        if token[1].strip() == '+':
            print("Parse successful, + recognized")
            position = position + 1
            token = tokens[position].split(',')
            token = checkComma(token)
        elif token[1].strip() == '-':
            print("Parse successful, / recognized")
            position = position + 1
            token = tokens[position].split('-')
            token = checkComma(token)
        else:
            print("Parsing error at: <expr'>")
        position = parse_term(tokens, position)
        token = updateToken(tokens, position)
        position = parse_expr_prime(tokens, position)
        token = updateToken(tokens, position)

    return position
        
def parse_term(tokens, position):
    print("successfully entered parse_term")
    token = tokens[position].split(',')
    token = checkComma(token)
    #first set{a,b,c,...,z, integers, doubles, (,}
    if token[0].strip() == "<Identifier>" or token[0].strip() == "<Int>" or token[0].strip() == "<Double>" or token[1].strip() == "(":
        position = parse_factor(tokens, position)
        token  = updateToken(tokens, position)
        position = parse_term_prime(tokens, position) 



    return position
    
def parse_term_prime(tokens, position):
    
    print("successfully entered parse_term_prime")
    token = tokens[position].split(',')
    lookahead_token = tokens[position + 1].split(',')
    print("Token at parse_term_prime")
    token = checkComma(token)
    lookahead_token = checkComma(lookahead_token)
    print("Token at parse_term_prime")
    print(token[0])
    print(token[1])

    #Follow set
    if lookahead_token[1].strip() == '+' or lookahead_token[1].strip() == '-':
        return position
    else: #first set
        if token[1].strip() == '*': #  * <factor> <term’>
            position = position + 1
            token = tokens[position].split(',')
            token = checkComma(token)
        elif token[0].strip() == "<Identifier>" or token[0].strip() == "<Int>" or token[0].strip() == "<Double>" or token[1].strip() == "(": #first of <factor>
            print("FEIUIEUFIUEHFE")
            position = parse_factor(tokens, position)
            token = updateToken(tokens, position)
            if token[1].strip() == "*" or token[1].strip() == "/" or token[1].strip() == "%": #first of term':
                position = parse_term_prime(tokens, position)
                token = updateToken(tokens, position)
            else:
                print("Parsing error at * <factor> <term’>")

        elif token[1].strip() == '%':
            print("Parse successful, + recognized")
            position = position + 1
            token = updateToken(tokens, position)

            

            position = parse_factor(tokens, position)
            token = updateToken(tokens, position)
            position = parse_term_prime(tokens, position)
            token = updateToken(tokens, position)

         
    return position
            
def parse_factor(tokens, position):
    print("successfully entered parse_factor")
    token = tokens[position].split(',')
    print("token at parse_factor")
    token = checkComma(token)
        
    #first of id
    if token[0].strip() == "<Identifier>":
        position = parse_id(tokens, position)
        token = updateToken(tokens, position)
        position = parse_factor_prime(tokens, position)
        token = updateToken(tokens, position)



    elif token[0].strip() == "<Int>" or token[0].strip() == "<Double>": #first of number
        position = parse_number(tokens, position)
        token = updateToken(tokens, position)
    elif token[1].strip() == '(':
        print("Parse successful, ( recognized")
        position = position + 1
        token = updateToken(tokens, position)
        position = parse_expr(tokens,position)
        token = updateToken(tokens, position)


        if token[1].strip() == ')':
            print("Parse successful, ) recognized")
            position = position + 1
            token = updateToken(tokens, position)

            

        else:
            print("Parsing error at: <factor> -> (<expr>)")
    
    elif token[0].strip() == "<Identifier>":
        print("TESTING2")
        position = parse_fname(token, position)
        token = updateToken(tokens, position)
        if token[1].strip() == '(':
            print("Parse successful, ( recognized")
            position = position + 1
            token = updateToken(tokens, position)
            position = parse_exprseq(tokens,position)
            token = updateToken(tokens, position)


            if token[1].strip() == ')':
                print("Parse successful, ) recognized")
                position = position + 1
                token = updateToken(tokens, position)


            else:
                print("Parsing error at: <factor> -> <fname>(<exprseq>)")
    
    return position

def parse_factor_prime(tokens, position):
    print("Successfully entered parse_factor_prime")
    token = tokens[position].split(',')
    token = checkComma(token)
    # first of var' {ε , [}
    if token[1].strip() == "[": # first of var'
        position = parse_var_prime(tokens, position)
        token = updateToken(tokens, position)

    elif token[1].strip() == "(":
        print("Parse successful, ( recognized")
        position = position + 1
        token = updateToken(tokens, position)
        position = parse_exprseq(tokens, position)
        token = updateToken(tokens, position)

        if token[1].strip() == ")":
            print("Parse successful, ) recognized")
            position = position + 1
            token = tokens[position].split(',')
            token = checkComma(token)
        else:
            print("Parsing error at <factor'> --> (<exprseq>)")
    else:
        print("Parsing error at parse_factor_prime")
    return position

def parse_number(tokens, position):
    print("successfully entered parse_number")
    token = tokens[position].split(',')
    token = checkComma(token)
    if token[0].strip() == "<Int>" or token[0].strip() == "<Double>":
        print("Parse successful, number recognized")
        position = position + 1
        token = tokens[position].split(',')
        token = checkComma(token)
        position = parse_exprseq(tokens,position)
        token = updateToken(tokens, position)

        

    return position
    
def parse_exprseq(tokens, position):
    print("successfully entered parse_exprseq")
    token = tokens[position].split(',')
    lookahead_token = tokens[position + 1].split(',')
    
    token = checkComma(token)
    lookahead_token = checkComma(lookahead_token)
        
    #follow set:
    if lookahead_token[1].strip() == ')':
        return position
    else: #first set
        if token[0].strip() == '<Identifier>' or token[0].strip() == '<Int>' or token[0].strip() == '<Double>' or token[1].strip() == '(':
            position = parse_expr(tokens, position)
            token = updateToken(tokens, position)

            position = parse_exprseq_prime(tokens, position)
            token = updateToken(tokens, position)

        else:
            print("Parsing error at <exprseq>")

    return position

def parse_exprseq_prime(tokens, position):
    print("successfully entered parse_exprseq_prime")
    token = tokens[position].split(',')
    lookahead_token = tokens[position + 1].split(',')
    token = checkComma(token)
    lookahead_token = checkComma(lookahead_token)
    #follow set
    if lookahead_token[1].strip() == ')':
        return position
    
    else:
        if token[1].strip() == ',':
            print("Parse successful, , recognized")
            position = position + 1
            token = tokens[position].split(',')
            token = checkComma(token)
            position = parse_exprseq(tokens, position)
            token = updateToken(tokens, position)

            
    return position
def parse_params_prime(tokens, position):
    print("successfully entered parse_params_prime")
    token = tokens[position].split(',')
    #follow set
    lookahead_token = tokens[position + 1].split(',')
    token = checkComma(token)
    lookahead_token = checkComma(lookahead_token)
    if lookahead_token[0].strip() == '<Operator>' and lookahead_token[1].strip() == ')':
        return position
    else: #first set
        if token[0].strip() == '<Operator>' and token[1].strip() == ',':
            position = position + 1
            token = tokens[position].split(',')
            token = checkComma(token)
            print("Parse successful, , recognized")
        position = parse_params(tokens, position)
        token = updateToken(tokens, position)

    return position

def parse_fname(tokens,position):
    print("successfully entered parse_fname")
    token = tokens[position].split(',')
    token = checkComma(token)
   

    if token[0].strip() == '<Identifier>':
        position = parse_id(tokens,position)
        token = updateToken(tokens, position)

    return position

def parse_id(tokens, position):
    print("successfully entered parse_id")
    position = parse_letter(tokens,position)
    token = updateToken(tokens, position)

    return position

def parse_id_prime(tokens, position):
    print("successfully entered parse_id_prime")
    token = tokens[position].split(',')
    lookahead_token = tokens[position + 1].split(',')
    token = checkComma(token)
    lookahead_token = checkComma(lookahead_token)
      
    
    if lookahead_token[1].strip() == '[' or lookahead_token[1].strip() == '(': # follow set
        return position
    else:
        if token[0].strip() == '<Identifier>':
            position = parse_letter(tokens, position)
            token = updateToken(tokens, position)
            position = parse_id_prime(tokens, position)
            token = updateToken(tokens, position)

        elif token[0].strip() == '<int>':
            position = parse_digit(tokens, position)
            token = updateToken(tokens, position)
            position = parse_id_prime(tokens, position)
            token = updateToken(tokens, position)

        else:
            print("Parse error at <id'>")
    
    return position

    
def parse_letter(tokens, position):
    print("successfully entered parse_letter")
    token = tokens[position].split(',')
    token = checkComma(token)
    
    if token[0].strip() == '<Identifier>':
        print("Parse successful: letter recognized")
        position = position + 1
        token = tokens[position].split(',')
        token = checkComma(token)
    else:
        print("Parse error at <letter>")


    return position

def parse_digit(tokens, position):
    print("successfully entered parse_digit")
    token = tokens[position].split(',')
    if tokens[0].strip() == '<int>':
        print("Parse successful: digit recognized")
        position = position + 1
        token = tokens[position].split(',')
        token = checkComma(token)
    else:
        print("Parse error at <digit>")

    return position

def parse_fdecls_prime(tokens, position):
    print("successfully entered parse_fdecls_prime")
    token = tokens[position  + 1].split(',')

    #follow set with epsilon: {ε, int, double}

    if token[1].strip() != "$":
        lookahead_token = tokens[position + 1].split(',')
        token = checkComma(token)
        lookahead_token = checkComma(lookahead_token)
        if lookahead_token[0] == "<Identifier>":
            if lookahead_token[1] == "int" or lookahead_token[1] == "Double" or lookahead_token[1] == "Duble":
                return position
            
    else:    # continue with first set    
        position = parse_fdec(tokens, position)
        token = updateToken(tokens, position)

        position = parse_fdecls_prime(tokens, position)
        token = updateToken(tokens, position)

    return position



def parse():
    #get list of tokens from output.txt
    tokens = []
    with open('output.txt', 'r') as file:
        for line in file:
            tokens.append(line.strip())
    tokens.append("END , $")
    #print(tokens)
    parse_program(tokens,0)
    return

def checkComma(token):
    if token[1].strip() ==  "": #Error where <Operator>, , gets split incorrectly. token[1] becomes nothing
            token[1] = ','
    return token

def updateToken(tokens,position):
    token = tokens[position].split(',')
    token = checkComma(token)
    return token
    
    

transition_table = csv_to_2Darray('CP471 -- Transition Table.csv') #Initialize transition table
keywords = keywords_to_list('keywords.txt') #initialize list of keywords
final_states = final_states_to_list('finalStates.txt')
decrement_final_states = [4,7,10,21,25,29,31,36,40,45,48,50,54,60,67,72,78,80,83]
file_name = input("Enter the name of the file you want to read from:")
lexical_analysis(transition_table,keywords,final_states,decrement_final_states,file_name)
print("Lexical Analysis Complete")

#Starting Phase 2
#LLTable = csv_to_2Darray('CP471 -- LL(1) Table - Sheet1.csv') #Initialize LL(1) parsing table
#print("-------------------------------------------STARTING PHASE 2-------------------------------------------")
#parse()
#print("Complete")
#token = "<def> , def"
#token = token.split(',')
#print(token[0])
#print(token[1].strip())
