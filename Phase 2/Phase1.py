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
    if (state in (2,3,4,6,7,9,10,11,12,13,14,15,16,17,18,19)): # Recognizes Operators 
        file.write("<Operator>")
    
    elif (state == 21): #Recognizes Identifiers
        file.write("<Identifier>")

    elif(state == 25): #Recognizes keyword and
        file.write("<and>")
    
    elif(state == 29): #Recognizes keyword def
        file.write("<def>")
    
    elif(state == 31): #Recognizes keyword do
        file.write("<do>")

    elif (state == 36): #Recognizes keyword else
        file.write("<else>")
    
    elif (state == 40): #Recognizes keyword fed
        file.write("<fed>")
    
    elif (state == 42): #Recognizes keyword fi
        file.write("<fi>")

    elif (state == 45): #Recognizes keyword if
        file.write("<if>")
    
    elif (state == 48): #Recognizes keyword od
        file.write("<od>")

    elif (state == 50): #Recognizes keyword or
        file.write("<or>")
    
    elif (state == 54): #Recognizes keyword not
        file.write("<not>")

    elif (state == 60): #Recognizes keyword print
        file.write("<print>")

    elif (state == 67): #Recognizes keyword return
        file.write("<return>")
    
    elif (state == 72): #Recognizes keyword then
        file.write("<then>")

    elif (state == 78): #Recognizes keyword while
        file.write("<while>")

    elif (state == 80): #Recognizes int
        file.write("<int>")
    
    elif (state == 83): #Recognizes double
        file.write("<double>")
    file.write("\n")


def lexical_analysis(transition_table, keywords, final_states, decrement_final_states, file_name):
    output_file = open('output.txt','w')
    error_file = open('errors.txt', 'w')
    with open(file_name, 'r') as file:
        buffer1 = file.read(BUFFER_SIZE)
        buffer2 = file.read(BUFFER_SIZE)
        print("Length of Buffer1")
        print(len(buffer1))
        print("Length of Buffer2")
        print(len(buffer2))
        while buffer1:
            current = transition_table[0][START]    #current state
            i = 0
            line_count = 1
            while i < len(buffer1):   #iterates through every char in buffer
                # Process character in buffer1
                #print(int(transition_table[ord(char)][current]))
                print(buffer1[i])
                previous = current
                current = int(transition_table[int(ord(buffer1[i]) - 1)][int(current)])
                print(current)
                if current in final_states: #Final state reached
                    print("final state reached: ")
                    getToken(current,output_file)

                    if current in decrement_final_states: #decrement one char back
                        print("FINAL STATE REACHED")
                        print(buffer1[i])
                        i = i - 1

                    
                    current = transition_table[0][START]
                elif current == -1: #Error
                    print("ERROR")
                    error_file.write("Char: " +  buffer1[i] + " line #: " + str(line_count))
                    current = transition_table[0][START]

                if (ord(buffer1[i]) == 10): # /n encountered
                    line_count += 1


                i+= 1
                
            

            

            buffer1 = buffer2
            print("-------------------------------------------BUFFER SWITCH-------------------------------------------")
            buffer2 = file.read(BUFFER_SIZE)
        output_file.close()
        error_file.close()




transition_table = csv_to_2Darray('CP471 -- Transition Table.csv') #Initialize transition table
keywords = keywords_to_list('keywords.txt') #initialize list of keywords
final_states = final_states_to_list('finalStates.txt')
decrement_final_states = [4,7,10,21,25,29,31,36,40,45,48,50,54,60,67,72,78,80,83]
file_name = input("Enter the name of the file you want to read from:")
lexical_analysis(transition_table,keywords,final_states,decrement_final_states,file_name)
print("Lexical Analysis Complete")
