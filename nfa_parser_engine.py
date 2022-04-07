import sys

if(sys.argv[0] == "nfa_parser_engine.py"):
    if(len(sys.argv) == 1):
        print("Not enough arguments")
        exit()
    elif(len(sys.argv) == 2):
        print("Loading and checking if the config file is valid")
    elif(len(sys.argv) > 2):
        print("Too many arguments")
        exit()

def nfa_parser_engine(*text_file):
    sigma = []
    states = []
    final_states = []
    transitions = []
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
    for linie in linii:
        if(linie != '#'):
            if(linie == "Sigma:\n"):
                reading_sigma = 1
            elif(linie == "States:\n"):
                reading_states = 1
            elif(linie == "Transitions:\n"):
                reading_transitions = 1
                for i in range(0, len(states)):
                    linie_none = []
                    for i in range(0, len(states)):
                        linie_none.append(None)
                    transitions.append(linie_none)
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
                            final_states.append(int(l[0][1]))
                        if('S' in l):
                            if (starting_state != None):
                                valid = 0
                                return sigma, states, transitions, starting_state, final_states, valid
                            else:
                                starting_state = int(l[0][1])
                elif(reading_transitions == 1):
                    linie = linie.replace(',', ' ')
                    linie = linie.replace(',', ' ')
                    l = linie.split()
                    if(l[0] in states and l[1][0] in sigma and l[2] in states):
                        coloana = int(l[0][1])
                        linie = int(l[2][1])
                        list = [l[1][0]]
                        if transitions[coloana - 1][linie - 1]:
                            transitions[coloana - 1][linie - 1].append(l[1][0])
                        else:
                            transitions[coloana - 1][linie - 1] = [l[1][0]]
                    else:
                        valid = 0
                        return sigma, states, transitions, starting_state, final_states, valid
    return sigma, states, transitions, starting_state, final_states, valid

if(sys.argv[0] == "nfa_parser_engine.py"):
    list = nfa_parser_engine()
    if(list[len(list) - 1] == 0):
        print("Input is not valid")
    else:
        print("Input is valid")