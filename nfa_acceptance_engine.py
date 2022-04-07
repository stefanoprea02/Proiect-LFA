import nfa_parser_engine
import sys

if(sys.argv[0] == "dfa_acceptance_engine.py"):
    if len(sys.argv) <= 2:
        print("Not enough arguments")
        exit()
    elif(len(sys.argv) == 3):
        print("Testing the acceptence of", sys.argv[2])
    elif(len(sys.argv) > 3):
        print("Too many arguments")
        print(sys.argv[2])
        exit()

def cautare(count, current_state, max_size):
    gasit = False
    acceptat = False
    for j in range(0, len(transitions[current_state - 1])):
        if(transitions[current_state - 1][j] and nfa[count] in transitions[current_state - 1][j]):
            if count == max_size - 1:
                current_state2 = j + 1
                for x in final_states:
                    if current_state2 == x:
                        acceptat = True
                        break
                if acceptat == True:
                    return True
            else:
                gasit = cautare(count + 1, j + 1, max_size)
                if gasit == True:
                    return True
    return gasit

sigma, states, transitions, starting_state, final_states, valid = nfa_parser_engine.nfa_parser_engine("nfa_config_file.txt")
if valid == 1:
    string = sys.argv[2]
    nfa = []
    for letter in string:
        nfa.append(letter)
    current_state = starting_state
    count = 0
    acceptat = cautare(count, current_state, len(nfa))
    if(acceptat == True):
        print("Input is accepted")
    else:
        print("Input is not accepted")
else:
    print("Input is not valid")