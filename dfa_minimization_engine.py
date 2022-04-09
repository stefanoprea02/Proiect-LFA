import sys
import dfa_parser_engine
import nfa_conversion_engine

if(sys.argv[0] == "dfa_parser_engine.py"):
    if(len(sys.argv) == 1):
        print("Not enough arguments")
        exit()
    elif(len(sys.argv) == 2):
        print("Loading and checking if the config file is valid")
    elif(len(sys.argv) > 2):
        print("Too many arguments")
        exit()

sigma, states, transitions, starting_state, final_states, valid = dfa_parser_engine.dfa_parser_engine("dfa_config_file.txt")

if valid == 1:

    # fac o matrice de dimensiune len(states) pe len(states)

    states_table = {}
    for state in states:
        list = {}
        for state2 in states:
            list[state2] = None
        states_table[state] = list

    # pun 1 pe pozitia [i][j] daca Qi apartine F si Qj nu apartine F sau invers

    for i in range(1, len(states)):
        for j in range(0, i):
            if states[i] not in final_states and states[j] in final_states:
                states_table[states[i]][states[j]] = 1
            elif states[i] in final_states and states[j] not in final_states:
                states_table[states[i]][states[j]] = 1

    # daca exista (Qi, Qj) != 0 atunci o sa pun (Qi, Qj) = 0
    # daca {δ(Qi, A), δ (Qi, A)} = 1
    # repet pana nu mai pot pune 1 nicaieri

    ok = True
    while ok:
        ok = False
        for state in states:
            for state2 in states:
                for litera in sigma:
                    if states_table[transitions[state][litera][0]][transitions[state2][litera][0]] == 1 and states_table[state][state2] != 1:
                        states_table[state][state2] = 1
                        ok = True

    new_dfa_states = []
    new_dfa_transitions = {}

    # combin toate nodurile in care nu este 1

    for i in range(1, len(states)):
        for j in range(0, i):
            if states_table[states[i]][states[j]] != 1:
                if new_dfa_states:
                    gasit = False
                    for state in new_dfa_states:
                        if states[i] in state[0] and states[j] not in state[0]:
                            list = state[0].split('-')
                            list.append(states[j])
                            new_dfa_states.remove(state)
                            gasit = True
                            break
                        elif states[j] in state[0] and states[i] not in state[0]:
                            list = state[0].split('-')
                            list.append(states[i])
                            new_dfa_states.remove(state)
                            gasit = True
                            break
                    if gasit == False:
                        ok = True
                        for state in new_dfa_states:
                            if states[j] in state[0] and states[i] in state[0]:
                                ok = False
                        if ok == True:
                            list = [states[j], states[i]]
                            new_dfa_states.append(['-'.join(list)])
                    else:
                        new_dfa_states.append(['-'.join(list)])
                else:
                    list = [states[j], states[i]]
                    new_dfa_states.append(['-'.join(list)])

    # vad daca au ramas noduri care nu se afla in new_dfa_transitions
    # daca da le adaug

    list = []
    for state in states:
        gasit = False
        for state2 in new_dfa_states:
            if state in state2[0]:
                gasit = True
        if gasit == False:
            list.append(state)

    for item in list:
        new_dfa_states.append([item])

    # fac noile transitii

    for state in transitions:
        for litera in sigma:
            for state2 in new_dfa_states:
                if state in state2[0]:
                    if state2[0] not in new_dfa_transitions:
                        new_dfa_transitions[state2[0]] = {}
                    for state3 in new_dfa_states:
                        if transitions[state][litera][0] in state3[0]:
                            if litera not in new_dfa_transitions[state2[0]]:
                                new_dfa_transitions[state2[0]][litera] = {}
                                new_dfa_transitions[state2[0]][litera] = state3

    for i in range(0, len(new_dfa_states)):
        new_dfa_states[i] = new_dfa_states[i][0]

    # caut nodul care era starting_state

    new_dfa_starting_state = None
    for state in new_dfa_states:
        if starting_state in state:
            new_dfa_starting_state = state

    # caut nodurile care erau final_states

    new_dfa_final_states = []
    for state in new_dfa_states:
        for final_state in final_states:
            if final_state in state:
                if state not in new_dfa_final_states:
                    new_dfa_final_states.append(state)

    # afisare

    nfa_conversion_engine.afisare(sigma, new_dfa_states, new_dfa_transitions, new_dfa_starting_state, new_dfa_final_states)
else:
    print("Input not valid.")