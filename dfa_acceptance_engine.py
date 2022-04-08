import dfa_parser_engine
import sys

if sys.argv[0] == "dfa_acceptance_engine.py":
    if len(sys.argv) <= 2:
        print("Not enough arguments")
        exit()
    elif len(sys.argv) == 3:
        print("Testing the acceptence of", sys.argv[2])
    elif len(sys.argv) > 3:
        print("Too many arguments")
        print(sys.argv[2])
        exit()

sigma, states, transitions, starting_state, final_states, valid = dfa_parser_engine.dfa_parser_engine("dfa_config_file.txt")
if valid == 1:
    string = sys.argv[2]
    dfa = tuple(string)
    current_state = starting_state

    #trecem prin fiecare litera din string si cautam daca nodul curent poate trece la alt nod prin acea litera

    for i in range(0, len(dfa)):
        gasit = False
        if transitions[current_state][dfa[i]]:
            current_state = transitions[current_state][dfa[i]][0]
            gasit = True
        else:
            break
    accepted = False

    #verificam daca nodul la care am ajuns este un nod final

    if gasit == True:
        for x in final_states:
            if current_state == x:
                print("Input accepted.")
                accepted = True
                break
    if accepted == False:
        print("Input not accepted.")
else:
    print("Input not valid.")