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
        file.write("<[> , [")
        
    elif (state == 85) : #Recognizes ] 
        file.write("<]> , ]")
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
def parse():
    #get list of tokens from output.txt
    tokens = []
    with open('output.txt', 'r') as file:
        for line in file:
            tokens.append(line.strip())
    tokens.append("$")
    print(tokens)
    #parse_prorgram(tokens)
    return




def parse_program(tokens, position): # <program>
    position = parse_fdecls(tokens, position)
    # Uncomment and implement the following lines as needed
    position = parse_declarations(tokens, position)
    position = parse_statement_seq(tokens, position)
    if tokens[position] == '$':
        print("Reached the end, parsing successful")
    return position

def parse_declarations(tokens,position):
    return

def parse_statement_seq(tokens,position):
    return

def parse_fdecls(tokens, position):
    token = token.strip()
    token = tokens[position].split(',')  # Corrected token extraction

    if token[0] == '<def>':  # Check for '<def>' token
        position = parse_fdec(tokens, position)  # Parse <fdec>
    else:
        print("Error in parsing: fdecls looking for <def>")
    # Parse <fdecls'> regardless
    position = parse_fdecls_prime(tokens, position) #Parse <fdecls'>
  
    return position

def parse_fdec(tokens, position):
    position = position + 1 #at this point def is terminal and to be here, current token needed to be def
    token = token.strip()
    token = tokens[position].split(',')
    if token[0] == '<identifier>': #Parse <type>
        position = parse_type(tokens,position) 
    
    
    if token[0] == '<identifier>': #Parse <id>
        position = parse_fname(tokens, position)
   
    
    if token[0] == '<Operator>':
        if token[2] == '(':
            position = position + 1 #terminal reached
            token = token.strip()
            token = tokens[position].split(',')
            
  
    if token[0] == 'identifier': #parse params
        position = parse_params(tokens, position) 
    
   
    if token[0] == '<Operator>':
        if token[2] == ')':
            position = position + 1 #terminal reached
            token = token.strip()
            token = tokens[position].split(',')
            
    
    if token[0] == '<Identifier>': #parse declarations
        position = parse_declarations(tokens, position)
        
    
    if token[0] == '<Identifier>' or token[0] == '<if>' or token[0] == '<while>' or token[0] == '<print>' or token[0] == 'return' or token[2] == ';':
        position = parse_statement_seq(tokens,position)
    
    
    if token[0] == '<Fed>':
        position = position + 1 #terminal reached
        token = token.strip()
        token = tokens[position].split(',')

    return position

def parse_type(tokens, position):
    #DOnt have the means to distinguish between two different identifiers titled int and double
    # for the sake of implementing this by the deadline, just going to assume its int
    position = position + 1
    token = token.strip()
    token = tokens[position].split(',')
    return position

def parse_params(tokens, position):
    if token[0] == '<identifier>':
        position = parse_type(tokens, position)
    return position

def parse_fname(tokens,position):
    
    if token[0] == '<Identifier>':
        position = parse_id(tokens,position)
    return position

def parse_id(tokens, position):
    position = parse_letter(tokens,position)
    return position

def parse_letter(tokens, position):
    position = position + 1 #Terminal reached
    token = token.strip()
    token = tokens[position].split(',')
    return position
def parse_fdecls_prime(tokens, position):
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
#parse()
#print("Complete")
#token = "<Operator> , temp"
#token = token.split(',')
