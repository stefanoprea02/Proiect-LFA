import dfa_parser_engine
import sys

if(sys.argv[0] == "dfa_acceptance_engine.py"):
    if(len(sys.argv) <= 2):
        print("Not enough arguments")
        exit()
    elif(len(sys.argv) == 3):
        print("Testing the acceptence of", sys.argv[2])
    elif(len(sys.argv) > 3):
        print("Too many arguments")
        print(sys.argv[2])
        exit()

sigma, states, transitions, starting_state, final_states, valid = dfa_parser_engine.dfa_parser_engine("dfa_config_file.txt")
if(valid == 1):
    string = sys.argv[2]
    dfa = []
    for letter in string:
        dfa.append(letter)
    current_state = starting_state
    count = 0
    for i in range(0, len(dfa)):
        gasit = False
        for j in range(0, len(transitions[current_state - 1])):
            if(dfa[i] == transitions[current_state - 1][j]):
                current_state = j + 1
                gasit = True
                break
        if(gasit == False):
            break
    accepted = False
    if(gasit == True):
        for x in final_states:
            if(current_state == x):
                print("Input accepted.")
                accepted = True
                break
    if(accepted == False):
        print("Input not accepted.")
else:
    print("Input not valid.")