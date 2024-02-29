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

def getToken(state,file): #function used to obtain token given a state

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
        file.write("<Identifier>")

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
        while buffer1:
            current = transition_table[0][START]    #current state
            i = 0
            line_count = 1
            while i < len(buffer1):   #iterates through every char in buffer
                # Process character in buffer1
                #print(buffer1[i])
                previous = current
                current = int(transition_table[int(ord(buffer1[i]) - 1)][int(current)])
                #print(current)
                if current in final_states: #Final state reached
                    #print("final state reached: ")
                    getToken(current,output_file)

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
def read_tokens_from_file(file_path):
    with open(file_path, 'r') as file:
        tokens = file.read().splitlines()
    tokens.append('$')
    return tokens

def parse(tokens, ll1_table):
    stack = ['$', '<program>']  # Assuming '$' signifies the end of input, and '<program>' is the start symbol.
    token_index = 0
    while stack:
        top = stack.pop()
        current_token = tokens[token_index]
        
        if top in terminals:  # Direct match with token
            if top == current_token:
                token_index += 1  # Consume token
            else:
                print(f"Error: expected {top}, found {current_token}")
                break
        elif top in non_terminals:
            # Find production rule: ll1_table[non-terminal][terminal]
            non_terminal_index = non_terminals.index(top)
            terminal_index = terminals.index(current_token)
            production_rule = ll1_table[non_terminal_index + 1][terminal_index]  # Offset by 1 due to headers
            
            if production_rule != 'N/A':
                # Reverse the production rule to push onto stack correctly
                for symbol in reversed(production_rule.split()):
                    if symbol != 'ε':
                        stack.append(symbol)
            else:
                print(f"Error: no rule for {top} with {current_token}")
                break
        else:
            print("Error: unexpected symbol")
            break
        
        if top == '$' and current_token == '$':
            print("Parsing successful!")
            return

    if stack:
        print("Parsing failed: stack not empty.")
    if token_index < len(tokens):
        print("Parsing failed: tokens remaining.")

# Example usage:
# tokens = read_tokens_from_file('output.txt')  # Implement this function to read tokens into a list
# ll1_table = read_ll1_table_from_csv('LL1_table.csv')  # Implement this function to read the LL(1) table into a 2D array
# parse(tokens, ll1_table)



transition_table = csv_to_2Darray('CP471 -- Transition Table.csv') #Initialize transition table
keywords = keywords_to_list('keywords.txt') #initialize list of keywords
final_states = final_states_to_list('finalStates.txt')
decrement_final_states = [4,7,10,21,25,29,31,36,40,45,48,50,54,60,67,72,78,80,83]
file_name = input("Enter the name of the file you want to read from:")
lexical_analysis(transition_table,keywords,final_states,decrement_final_states,file_name)
print("Lexical Analysis Complete")

#Starting Phase 2
#LLTable = csv_to_2Darray('CP471 -- LL(1) Table - Sheet1.csv') #Initialize LL(1) parsing table
#tokens = Parse('output.txt', LLTable)
#print("Complete")
