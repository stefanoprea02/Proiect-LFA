import sys

if(sys.argv[0] == "dfa_parser_engine.py"):
    if(len(sys.argv) == 1):
        print("Not enough arguments")
        exit()
    elif(len(sys.argv) == 2):
        print("Loading and checking if the config file is valid")
    elif(len(sys.argv) > 2):
        print("Too many arguments")
        exit()

def dfa_parser_engine(*text_file):

    # initializam valorile din dfa

    sigma = []
    states = []
    final_states = []
    transitions = {}
    if(text_file):
        file = open(text_file[0], 'r')
    else:
        file = open(sys.argv[1], 'r')
    linii = file.readlines()
    reading_sigma = 0
    reading_states = 0
    reading_transitions = 0
    starting_state = None
    valid = 1

    #citim linie cu linie

    for linie in linii:
        if(linie != '#'):
            if(linie == "Sigma:\n"):
                reading_sigma = 1
            elif(linie == "States:\n"):
                reading_states = 1
            elif(linie == "Transitions:\n"):

                # facem un dictionar pentru fiecare nod

                reading_transitions = 1
                for i in range(0, len(states)):
                    dict = {}
                    for j in range(0, len(sigma)):
                        dict[sigma[j]] = None
                    transitions[states[i]] = dict
            elif(linie == "End\n" or linie == "End"):
                reading_sigma = 0
                reading_states = 0
                reading_transitions = 0
            else:
                if(reading_sigma == 1):
                    l = linie.split()
                    sigma.append(l[0])
                elif(reading_states == 1):
                    l = linie.split()
                    states.append(l[0])
                    if(len(l) > 1):
                        if('F' in l):
                            final_states.append(l[0])
                        if('S' in l):
                            if (starting_state != None):
                                valid = 0
                                return sigma, states, transitions, starting_state, final_states, valid
                            else:
                                starting_state = l[0]
                elif(reading_transitions == 1):
                    linie = linie.replace(',', ' ')
                    linie = linie.replace(',', ' ')
                    l = linie.split()
                    if(l[0] in states and l[1] in sigma and l[2] in states):
                        if transitions[l[0]][l[1]]:
                            valid = 0
                            return sigma, states, transitions, starting_state, final_states, valid
                        else:
                            transitions[l[0]][l[1]] = [l[2]]
                    else:
                        valid = 0
                        return sigma, states, transitions, starting_state, final_states, valid
    return sigma, states, transitions, starting_state, final_states, valid

if(sys.argv[0] == "dfa_parser_engine.py"):
    list = dfa_parser_engine()
    if(list[len(list) - 1] == 0):
        print("Input is not valid")
    else:
        print("Input is valid")