import sys
import nfa_parser_engine

if(sys.argv[0] == "nfa_conversion_engine.py"):
    if(len(sys.argv) == 1):
        print("Not enough arguments")
        exit()
    elif(len(sys.argv) == 2):
        print("Converting nfa to dfa")
    elif(len(sys.argv) > 2):
        print("Too many arguments")
        exit()

def functie(dfa_transitions, state):
    for litera in sigma:

        #luam fiecare nod care din care merge nodul curent si il punem intr-un set pe care il sortam

        states2 = state.split('-')
        list = set()
        for x in states2:
            if transitions[x][litera]:
                for y in transitions[x][litera]:
                    list.update([y])
        list2 = [x for x in list]
        list = list2
        list = sorted(list, key=lambda x: x[1])
        dfa_states.update(['-'.join(list)])
        dfa_transitions[state][litera] = list

        #luam toate nodurile din lista si le adunam intr-un singur nod
        #daca acest nod e format din mai multe noduri verificam daca a mai fost format inainte
        #daca nu acesta devine un nou nod in dfa si apelam iar functia
        #daca nodul nu e format din mai multe noduri atunci il adaugam la dfa_transition

        if len(list) > 1:
            newState = "-".join(list)
            if newState not in dfa_transitions:
                dfa_transitions[newState] = {}
                functie(dfa_transitions, newState)
        elif len(list) == 1:
            if list:
                dfa_transitions[list[0]] = {}
                dfa_transitions[list[0]][litera] = transitions[list[0]][litera]
                for state in dfa_transitions:
                    state2 = state.split('-')
                    if len(state2) == 1:
                        for litera in sigma:
                            if transitions[state][litera]:
                                if litera not in dfa_transitions[state]:
                                    dfa_transitions[state][litera] = {}
                                    dfa_transitions[state][litera] = transitions[state][litera]

def afisare(*t):
    sigma = t[0]
    dfa_states = t[1]
    dfa_transitions = t[2]
    dfa_starting_state = t[3]
    dfa_final_states = t[4]
    print("#")
    print("#")
    print("#")
    print("Sigma:")
    for litera in sigma:
        print("    ", litera)
    print("End")
    print("#")
    print("#")
    print("#")
    print("States:")
    for state in dfa_states:
        if state in dfa_starting_state:
            print("    ", state, ", S")
        elif state in dfa_final_states:
            print("    ", state, ", F")
        else:
            print("    ", state)
    print("End")
    print("#")
    print("#")
    print("#")
    print("Transitions:")
    for state in dfa_transitions:
        for litera in sigma:
            if litera in dfa_transitions[state]:
                list = '-'.join(dfa_transitions[state][litera])
                print("    ", state, ",", litera, ",", list)
    print("End")
    print("#")
    print("#")
    print("#")

if(sys.argv[0] == "nfa_conversion_engine.py"):
    sigma, states, transitions, starting_state, final_states, valid = nfa_parser_engine.nfa_parser_engine("nfa_config_file.txt")
    if valid == 1:

        # initializam valorile noului dfa

        dfa_sigma = sigma
        dfa_starting_state = starting_state
        dfa_final_states = set()
        dfa_states = set()
        dfa_states.update([states[0]])
        dfa_transitions = {}
        dfa_transitions[states[0]] = transitions[states[0]]

        state = states[0]
        for litera in sigma:
            if transitions[state][litera]:
                list = transitions[state][litera]
            dfa_states.update(['-'.join(list)])

            #vedem daca nodul curent merge in mai multe noduri

            if len(list) > 1:

                #daca da atunci creem un nou nod care contine toate nodurile in care nodul curent merge

                newState = "-".join(list)
                dfa_transitions[newState] = {}
                functie(dfa_transitions, newState)
            elif len(list) == 1:

                #daca nu copiem nodul in care merge nodul curent si il punem in dfa_transitions

                dfa_transitions[list[0]] = {}
                dfa_transitions[list[0]][litera] = transitions[list[0]][litera]
                functie(dfa_transitions, list[0])

        #cautam toate nodurile formate din mai multe noduri care contin un nod final

        for state in dfa_transitions:
            for litera in sigma:
                list = dfa_transitions[state][litera]
                final_state_in_list = False
                for final_state in final_states:
                    if list and final_state in list:
                        final_state_in_list = True
                    else:
                        if list:
                            pass
                        else:
                            dfa_transitions[state].pop(litera)
                if final_state_in_list == True:
                    dfa_final_states.update(["-".join(list)])

        while "" in dfa_states:
            dfa_states.remove("")

        for state in dfa_transitions:
            for litera in sigma:
                if litera in dfa_transitions[state]:
                    dfa_transitions[state][litera] = ['-'.join(dfa_transitions[state][litera])]

        dfa_states = sorted(dfa_states, key=lambda x: x[1])
        afisare(dfa_sigma, dfa_states, dfa_transitions, dfa_starting_state, dfa_final_states)
    else:
        print("Input is not valid")