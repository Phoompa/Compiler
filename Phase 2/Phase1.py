import csv
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
        file.write("<Operator> , <=")
    
    elif (state == 3): #Recognizes operator <>
        file.write("<Operator> , <>")
        
    elif (state == 4): #Recognizes operator <
        file.write("<Operator> , <")
        
    elif (state == 6): #Recognizes operator ==
        file.write("<Operator> , ==")
    
    elif (state == 7): #Recognizes operator =
        file.write("<Operator> , =")
        
    elif (state == 9): #Recognizes operator >=
        file.write("<Operator> , >=")
    
    elif (state == 10): #Recognizes operator >
        file.write("<Operator> , >")
        
    elif (state == 11): #Recognizes operator +
        file.write("<Operator> , +")
        
    elif (state == 12): #Recognizes operator -
        file.write("<Operator> , -")
        
    elif (state == 13): #Recognizes operator *
        file.write("<Operator> , *")
    
    elif (state == 14): #Recognizes operator /
        file.write("<Operator> , /")
    
    elif (state == 15): #Recognizes operator %
        file.write("<Operator> , %")
    
    elif (state == 16): #Recognizes operator ,
        file.write("<Operator> , ,")
    
    elif (state == 17): #Recognizes operator ;
        file.write("<Operator> , ;")
        
    elif (state == 18): #Recognizes operator (
        file.write("<Operator> , (")
        
    elif (state == 19): #Recognizes operator )
        file.write("<Operator> , )")        
        
    elif (state == 21): #Recognizes Identifiers
        file.write("<Identifier> , " + IdentifierString)

    elif(state == 25): #Recognizes keyword and
        file.write("<and> , and")
    
    elif(state == 29): #Recognizes keyword def
        file.write("<def> , def")
    
    elif(state == 31): #Recognizes keyword do
        file.write("<do> , do")

    elif (state == 36): #Recognizes keyword else
        file.write("<else> , else")
    
    elif (state == 40): #Recognizes keyword fed
        file.write("<fed> , fed")
    
    elif (state == 42): #Recognizes keyword fi
        file.write("<fi> , fi")

    elif (state == 45): #Recognizes keyword if
        file.write("<if> , if")
    
    elif (state == 48): #Recognizes keyword od
        file.write("<od> , od")

    elif (state == 50): #Recognizes keyword or
        file.write("<or> , or")
    
    elif (state == 54): #Recognizes keyword not
        file.write("<not> , not")

    elif (state == 60): #Recognizes keyword print
        file.write("<print> , print")

    elif (state == 67): #Recognizes keyword return
        file.write("<return> , return")
    
    elif (state == 72): #Recognizes keyword then
        file.write("<then> , then")

    elif (state == 78): #Recognizes keyword while
        file.write("<while> , while")

    elif (state == 80): #Recognizes int
        file.write("<int>, int")
    
    elif (state == 83): #Recognizes double
        file.write("<double> , double")
        
    elif (state == 84) : #Recognizes [
        file.write("<Operator> , [")
        
    elif (state == 85) : #Recognizes ] 
        file.write("<Operator> , ]")
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
                            print("her")
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
    
    token = tokens[position].split(',')
    position = parse_fdecls(tokens, position)
    position = parse_declarations(tokens, position)
    position = parse_statement_seq(tokens, position)
    token = tokens[position].split(',')

    if token[1] == '$':
        print("Reached the end, parsing successful")
    return position

def parse_declarations(tokens,position):
    lookahead_token = tokens[position + 1].split(',')
    token = tokens[position].split(',')

    if lookahead_token[0] == '<while>' or lookahead_token[0] == '<if>' or lookahead_token[0] == '<print>' or lookahead_token[0] == '<return>' or lookahead_token[0] == '<Identifier>' : #follow set
        return position
    else:
        if token[0] == '<Identifier>':
            if token[1] == 'int' or token[1] == 'double' or token[1] == 'duble':
                position = parse_decl(tokens, position)
                if token[1] == ';':
                    position = position + 1
                    token = tokens[position].split(',')
                    print("Parse successful: ; recognized")
                    
                position = parse_declarations_prime(tokens, position)
        else:
            print("Parsing error at <declarations> --> <decl>; <declarations> ")
    
    return position

def parse_declarations_prime(tokens,position):
    lookahead_token = tokens[position + 1].split(',')
    token = tokens[position].split(',')

    if lookahead_token[0] == '<while>' or lookahead_token[0] == '<if>' or lookahead_token[0] == '<print>' or lookahead_token[0] == '<return>' or lookahead_token[0] == '<Identifier>' : #follow set
        return position
    else:
        if token[0] == '<Identifier>':
            if token[1] == 'int' or token[1] == 'double' or token[1] == 'duble':
                position = parse_decl(tokens, position)
                if token[1] == ';':
                    position = position + 1
                    token = tokens[position].split(',')
                    print("Parse successful: ; recognized")
                    
                    
                position = parse_declarations_prime(tokens, position)
        else:
            print("Parsing error at <declarations'> --> <decl>; <declarations'> ")
    
    return position

def parse_decl(tokens, position):
    token = tokens[position].split(',')

    if token[0] == '<Identifier>':
        if token[1] == 'int' or token[1] == 'double' or token[1] == 'duble':
            position = parse_type(tokens,position)
            position = parse_varlist(tokens, position)

    return position

def parse_varlist(tokens, position):
    token = tokens[position].split(',')

    if token[0] == '<Identifier>':
        position = parse_var(tokens, position)
        position = parse_varlist_prime(tokens,position)
    return position

def parse_varlist_prime(tokens, position):
    lookahead_token = tokens[position + 1].split(',')
    token = tokens[position].split(',')

    if lookahead_token[1] == ';': #follow set
        return position
    else: #first set
        if token[1] == ',':
            print("Parse successful: , recognized")
            position = position + 1
            token = tokens[position].split(',')
        else:
            print("Error at <varlist'>")
        position = parse_varlist(tokens, position)

    return position

def parse_statement_seq(tokens,position):
    token = tokens[position].split(',')
    if token[0] == '<if>' or token[0] == '<Identifier>' or token[0] == '<while>'  or token[0] == '<print>' or token[0] == '<return>' or token[1] == ';':
        position = parse_statement(tokens, position)
        position = parse_statement_seq_prime(tokens, position)
    return position

def parse_statement_seq_prime(tokens, position):
    lookahead_token = tokens[position + 1].split(',')
    token = tokens[position].split(',')
    if lookahead_token[0] == '<fi>' or lookahead_token[0] == '<else>' or lookahead_token[0] == '<od>' or lookahead_token[0] == '<fed>' or lookahead_token[1] == '$':#follow set
        return position
    else: # first set
        if token[1] == ';':
            print("Parse successful: ; recognized")
            position = position + 1
            token = tokens[position].split(',')
        else:
            print("Parse error at: <statement_seq'>")
        position = parse_statement_seq(tokens, position)

    return position

def parse_statement(tokens, position):
    lookahead_token = tokens[position + 1].split(',')
    token = tokens[position].split(',')

    if lookahead_token[1] == ';':#follow set
        return position
    #elif below for: if <bexpr> then <statement_seq><statement'>
    elif token[0] == '<if>':
        print("Parse successful: if recognized")
        position = position + 1
        token = tokens[position].split(',')
        position = parse_bexpr(tokens, position)
        if token[0] == '<then>':
            print("Parse successful: <then> recognized")
            position = position + 1
            token = tokens[position].split(',')
        else:
            print("Parse error: <statement>")
        position = parse_statement_seq(tokens, position)
        position = parse_statement_prime(tokens, position)

    #elif below for: <var> = <expr>
    elif token[0] == '<Identifier>':
        position = parse_var(tokens,position)
        if token[1] == '=':
            print("Parse successful: = recognized")
            position = position + 1
            token = tokens[position].split(',')

        else:
            print("Parse error at <statement>")
        position = parse_expr(tokens, position)

    #elif below for: While <bexpr> do <statement_seq> od
    elif token[0] == '<while>':
        print("Parse successful: while recognized")
        position = position + 1
        token = tokens[position].split(',')
        position = parse_bexpr(tokens, position)
        if token[0] == '<do>':
            print("Parse successful: do recognized")
            position = position + 1
            token = tokens[position].split(',')
        else:
            print("Parse error at <statement>")
        position = parse_statement_seq(tokens, position)
        if token[0] == '<od>':
            print("Parse successful: od recognized")
            position = position + 1
            token = tokens[position].split(',')
        else:
            print("Parse error at <statement>")
    #elif for: print <expr>
    elif token[0] == '<print>':
        print("Parse successful: print recognized")
        position = position + 1
        token = tokens[position].split(',')
        position = parse_expr(tokens, position)
    #elif for: Return <expr> 
    elif token[0] == '<return>':
        print("Parse successful: return recognized")
        position = position + 1
        token = tokens[position].split(',') 
        position = parse_expr(tokens, position)      
    return position

def parse_bexpr(tokens, position):
    token = tokens[position].split(',')
    if token[1] == '(' or token[0] == '<not>':
        position = parse_bterm(tokens, position)
        position = parse_bexpr_prime(tokens, position)
    else:
        print("Parse error at <bexpr>")
    return position

def parse_bexpr_prime(tokens, position):
    lookahead_token = tokens[position + 1].split(',')
    token = tokens[position].split(',')
    if lookahead_token[1] == ')' or lookahead_token[0] == '<then>' or lookahead_token[0] == '<do>':#follow set
        return position
    
    else: #first set
        if token[0] == '<or>':
            print("Parse successful: or recognized")
            position = position + 1
            token = tokens[position].split(',')
        else:
            print("Parse error at <bexpr'>")
            position = parse_bterm(tokens, position)
            position = parse_bexpr_prime(tokens,position)

    return position

def parse_bterm(tokens, position):
    token = tokens[position].split(',')
    if token[1] == '(' or token[0] == '<not>':
        position = parse_bfactor(tokens, position)
        position = parse_bterm_prime(tokens, position)
    else:
        print("Parse error at <bterm>")
    return position

def parse_bterm_prime(tokens, position):
    lookahead_token = tokens[position + 1].split(',')
    token = tokens[position].split(',')

    if lookahead_token[0] == '<or>':#follow set
        return position
    
    else: #first set
        if token[0] == '<and>':
            print("Parse successful: and recognized")
            position = position + 1
            token = tokens[position].split(',')
        else:
            print("Parse error at <bterm'>")
        
        position = parse_bfactor(tokens, position)
        position = parse_bterm_prime(tokens, position)

    return position

def parse_bfactor(tokens, position):
    token = tokens[position].split(',')
    if token[1] == '(':
        print("Parse successful: ( recognized")
        position = parse_bexpr(tokens, position)
        if token[1] == ')':
            print("Parse successful: ) recognized")
            position = position + 1
            token = tokens[position].split(',')
        else:
            print("Parse error at <bfactor>")
    elif token[1] == '(':
        print("Parse successful: ( recognized")
        position = position + 1
        token = tokens[position].split(',')
        position = parse_expr(tokens, position)
        position = parse_comp(tokens, position)
        position = parse_expr(tokens, position)
        if token[1] == ')':
            print("Parse successful: ) recognized")
            position = position + 1
            token = tokens[position].split(',')
        else:
            print("Parse error at <bfactor>")

    elif token[0] == '<not>':
        print("Parse successful: not recognized")
        position = position + 1
        token = tokens[position].split(',')
        position = parse_bfactor(tokens, position)
    else:
        print("Parse error at <bfactor>")
    return position

def parse_comp(tokens, position):
    token = tokens[position].split(',')

    if token[1] == '<':
        print("Parse successful: < recognized")
        position = position + 1
        token = tokens[position].split(',')
    elif token[1] == '>':
        print("Parse successful: > recognized")
        position = position + 1
        token = tokens[position].split(',')
    elif token[1] == '==':
        print("Parse successful: == recognized")
        position = position + 1
        token = tokens[position].split(',')
    elif token[1] == '<=':
        print("Parse successful: <= recognized")
        position = position + 1
        token = tokens[position].split(',')
    elif token[1] == '>=':
        print("Parse successful: >= recognized")
        position = position + 1
        token = tokens[position].split(',')
    elif token[1] == '<>':
        print("Parse successful: <> recognized")
        position = position + 1
        token = tokens[position].split(',')
    else:
        print("Parse error at <comp>")


    return position

def parse_statement_prime(tokens, position):
    token = tokens[position].split(',')
    if token[0] == '<fi>':
        print("Parse successful: fi recognized")
        position = position + 1
        token = tokens[position].split(',')
    elif token[0] == '<else>':
        print("Parse successful: else recognized")
        position = position + 1
        token = tokens[position].split(',')
        position = parse_statement_seq(tokens, position)
        if token[0] == '<fi>':
            print("Parse successful: fi recognized")
            position = position + 1
            token = tokens[position].split(',')
        else:
            print("Parse error at <statement'>")
    else:
        print("Parse error at <statement'>")
    return position

def parse_fdecls(tokens, position):
    token = tokens[position].split(',')  
    print(position)
    print(token[0])
    print(token[1])
    print(type(token[0]))
    if token[0] == '<def>\n':

        print("successfully entered <def>")
        position = parse_fdec(tokens, position)
        token = tokens[position].split(',')  
    if token[1] == ';':
        position = position + 1
        token = tokens[position].split(',')
        print("Parse successful, ; recognized")
    else:
        print("Parsing error at: <fdecls> -> <fdec>;<fdecls'>")
    position = parse_fdecls_prime(tokens, position)
        
    return position

def parse_fdec(tokens, position):
    print("Entered Fdec")
    position = position + 1 #at this point def is terminal and to be here, current token needed to be def
    
    token = tokens[position].split(',')
    if token[0] == '<identifier>': #Parse <type>
        position = parse_type(tokens,position) 
        token = tokens[position].split(',')

    
    
    if token[0] == '<identifier>': #Parse <id>
        position = parse_fname(tokens, position)
        token = tokens[position].split(',')

   
    
    if token[0] == '<Operator>':
        if token[1] == '(':
            position = position + 1 #terminal reached
            token = tokens[position].split(',')
            
  
    if token[0] == 'identifier': #parse params
        position = parse_params(tokens, position)
        token = tokens[position].split(',')
 
    
   
    if token[0] == '<Operator>':
        if token[1] == ')':
            position = position + 1 #terminal reached
            token = tokens[position].split(',')
            
    
    if token[0] == '<Identifier>': #parse declarations
        position = parse_declarations(tokens, position)
        token = tokens[position].split(',')

    print(token[1])
    if token[0] == '<Identifier>' or token[0] == '<if>' or token[0] == '<while>' or token[0] == '<print>' or token[0] == 'return' or token[1] == ';':
        position = parse_statement_seq(tokens,position)
        token = tokens[position].split(',')

    
    
    if token[0] == '<Fed>':
        position = position + 1 #terminal reached
        token = tokens[position].split(',')

    return position

def parse_type(tokens, position):
    if token[1] == "int":
        print("Parse successful, int identifier recognized")
    if token[1] == "double" or token[1] == "duble":
        print("Parse successful, int recognized")
    position = position + 1
    token = tokens[position].split(',')

    
    
    return position

def parse_params(tokens, position):
    token = tokens[position].split(',')
    lookahead_token = tokens[position + 1].split(',')
    if lookahead_token[0] == '<Operator>' and lookahead_token[1] == ')': #follow set
        return position
    else: #first set
        if token[0] == '<Identifier>':
            if token[1] == 'int' or token[1] == 'double' or token[1] == 'duble':
                position = parse_type(tokens, position)
                position = parse_var(tokens, position)
                position = parse_params_prime(tokens, position)
    return position

def parse_var(tokens, position):
    token = tokens[position].split(',')
    if token[0] == '<Identifier>':
        position = parse_id(tokens, position)
        position = parse_var_prime(tokens, position)
    else:
        print("Parsing Error at <var>")
    return position

def parse_var_prime(tokens, position):
    token = tokens[position].split(',')
    lookahead_token = tokens[position + 1].split(',')
    if lookahead_token[1] == '=' or lookahead_token[1] == ',' or lookahead_token[1] == '*' or lookahead_token[1] == '/' or lookahead_token[1] == '%': #follow set
        return position
    else:
        if token[0] == '<Operator>' and token[1] == '[':
            print("Parse successful, [] recognized")
            position = position + 1
            token = tokens[position].split(',')
        position = parse_expr(tokens, position)
        if token[0] == '<Operator>' and token[1] == ']':
            print("Parse successful, [] recognized")
            position = position + 1
            token = tokens[position].split(',')   

    return position

def parse_expr(tokens, position):
    token = tokens[position].split(',')
    if token[0] == "<Identifier>" or token[0] == "<Int>" or token[0] == "<Double>":
        position = parse_term(tokens, position)
        position = parse_expr_prime(tokens, position)
    elif token[0] == "<Operator>" and token[1] == '(':
        position = parse_term(tokens, position)
        position = parse_expr_prime(tokens, position)
    return position

def parse_expr_prime(tokens, position):
    token = tokens[position].split(',')
    lookahead_token = tokens[position + 1].split(',')
    #follow set
    if lookahead_token[1] == ']' or lookahead_token[1] == '<' or lookahead_token[1] == '>' or lookahead_token[1] == '==' or lookahead_token[1] == '<=' or lookahead_token[1] == '>=' or lookahead_token[1] == '<>' or lookahead_token[1] ==  ')' or lookahead_token[1] == ',' or lookahead_token[1] == ';':
        return position
    else:
        if token[1] == '+':
            print("Parse successful, + recognized")
            position = position + 1
            token = tokens[position].split(',')
        elif token[1] == '-':
            print("Parse successful, / recognized")
            position = position + 1
            token = tokens[position].split('-')
        else:
            print("Parsing error at: <expr'>")
        position = parse_term(tokens, position)
        position = parse_expr_prime(tokens, position)
    return position
        
def parse_term(tokens, position):
    token = tokens[position].split(',')
    if token[0] == "<Identifier>" or token[0] == "<Int>" or token[0] == "<Double>":
        position = parse_factor(tokens, position)
        position = parse_term_prime(tokens, position)
    elif token[0] == "<Operator>" and token[1] == '(':
        position = parse_factor(tokens, position)
        position = parse_term_prime(tokens, position)
    else:
        print("parsing error at: <term>")

    return position
    
def parse_term_prime(tokens, position):
    token = tokens[position].split(',')
    lookahead_token = tokens[position + 1].split(',')

    #Follow set
    if lookahead_token[1] == '+' or lookahead_token[1] == '-':
        return position
    else: #first set
        if token[1] == '*':
            print("Parse successful, * recognized")
            position = position + 1
            token = tokens[position].split(',')
        elif token[1] == '/':
            print("Parse successful, / recognized")
            position = position + 1
            token = tokens[position].split(',')
        elif token[1] == '%':
            print("Parse successful, + recognized")
            position = position + 1
            token = tokens[position].split(',')
        position = parse_factor(tokens, position)
        position = parse_term_prime(tokens, position)
         
    return position
            
def parse_factor(tokens, position):
    token = tokens[position].split(',')

    #first of var
    if token[0] == "<Identifier>":
        position = parse_var(tokens, position)
    elif token[0] == "<Int>" or token[0] == "<Double>": #first of number
        position = parse_number(tokens, position)
    elif token[1] == '(':
        print("Parse successful, ( recognized")
        position = position + 1
        token = tokens[position].split(',')
        position = parse_expr(tokens,position)
        token = tokens[position].split(',')
        if token[1] == ')':
            print("Parse successful, ) recognized")
            position = position + 1
            token = tokens[position].split(',')
        else:
            print("Parsing error at: <factor> -> (<expr>)")
    
    elif token[0] == "<Identifier>":
        position = parse_fname(token, position)
        token = tokens[position].split(',')
        if token[1] == '(':
            print("Parse successful, ( recognized")
            position = position + 1
            token = tokens[position].split(',')
            position = parse_exprseq(tokens,position)
            token = tokens[position].split(',')
            if token[1] == ')':
                print("Parse successful, ) recognized")
                position = position + 1
                token = tokens[position].split(',')
            else:
                print("Parsing error at: <factor> -> <fname>(<exprseq>)")
    
    return position

def parse_number(tokens, position):
    token = tokens[position].split(',')
    if token[0] == "<Int>" or token[0] == "<Double>":
        print("Parse successful, number recognized")
        position = position + 1
        token = tokens[position].split(',')
        position = parse_exprseq(tokens,position)
        

    return position
    
def parse_exprseq(tokens, position):
    token = tokens[position].split(',')
    lookahead_token = tokens[position + 1].split(',')
    #follow set:
    if lookahead_token[1] == ')':
        return position
    else: #first set
        if token[0] == '<Identifier>' or token[0] == '<Int>' or token[0] == '<Double>' or token[1] == '(':
            position = parse_expr(tokens, position)
            token = tokens[position].split(',')
            position = parse_exprseq_prime(tokens, position)
        else:
            print("Parsing error at <exprseq>")

    return position

def parse_exprseq_prime(tokens, position):
    token = tokens[position].split(',')
    lookahead_token = tokens[position + 1].split(',')
    #follow set
    if lookahead_token[2] == ')':
        return position
    
    else:
        if token[1] == ',':
            print("Parse successful, , recognized")
            position = position + 1
            token = tokens[position].split(',')
            position = parse_exprseq(tokens, position)
            
    return position
def parse_params_prime(tokens, position):
    token = tokens[position].split(',')

    #follow set
    lookahead_token = tokens[position + 1].split(',')
    if lookahead_token[0] == '<Operator>' and lookahead_token[1] == ')':
        return position
    else: #first set
        if token[0] == '<Operator>' and token[1] == ',':
            position = position + 1
            token = tokens[position].split(',')
            print("Parse successful, , recognized")
        position = parse_params(tokens, position)
    return position

def parse_fname(tokens,position):
    token = tokens[position].split(',')

    if token[0] == '<Identifier>':
        position = parse_id(tokens,position)
    return position

def parse_id(tokens, position):
    position = parse_letter(tokens,position)
    return position

def parse_id_prime(tokens, position):
    token = tokens[position].split(',')
    lookahead_token = tokens[position + 1].split(',')
    if lookahead_token[1] == '[' or lookahead_token[1] == '(': # follow set
        return position
    else:
        if token[0] == '<Identifier>':
            position = parse_letter(tokens, position)
            position = parse_id_prime(tokens, position)
        elif token[0] == '<int>':
            position = parse_digit(tokens, position)
            position = parse_id_prime(tokens, position)
        else:
            print("Parse error at <id'>")
    
    return position

    
def parse_letter(tokens, position):
    token = tokens[position].split(',')
    if token[0] == '<Identifier>':
        print("Parse successful: letter recognized")
        position = position + 1
        token = tokens[position].split(',')
    else:
        print("Parse error at <letter>")


    return position

def parse_digit(tokens, position):
    token = tokens[position].split(',')
    if tokens[0] == '<int>':
        print("Parse successful: digit recognized")
        position = position + 1
        token = tokens[position].split(',')
    else:
        print("Parse error at <digit>")

    return position

def parse_fdecls_prime(tokens, position):
    token = tokens[position  + 1].split(',')
    #follow set with epsilon
    if token[1] != "$":
        lookahead_token = tokens[position + 1].split(',')
        if lookahead_token[0] == 'Identifier':
            if lookahead_token[1] == 'int' or lookahead_token[1] == 'double' or lookahead_token[1] == 'duble':
                return position
            
    else:    # continue with first set    
        position = parse_fdec(tokens, position)
        position = parse_fdecls_prime(tokens, position)
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
parse()
print("Complete")
token = "<def> , def"
token = token.split(',')
print(token[0])
print(token[1])
