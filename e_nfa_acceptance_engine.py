import nfa_parser_engine
import sys

if(sys.argv[0] == "e_nfa_acceptance_engine.py"):
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

    #verificam daca nodul curent poate trece la alte noduri prin e, daca da trecem la acel nod prin apelul functie

    if transitions[current_state]['e']:
        if count == max_size - 1:
            for state in transitions[current_state]['e']:
                if state in final_states:
                    acceptat = True
                    return acceptat
                    break
        for state in transitions[current_state]['e']:
            gasit = cautare(count, state, max_size)
            if gasit == True:
                return True

    #verificam daca putem trece la alt nod prin litera din string la care am ajuns
    #daca da trecem la ea, iar daca nu returnam fals

    if transitions[current_state][nfa[count]]:
        if count == max_size - 1:
            for state in transitions[current_state][nfa[count]]:
                if state in final_states:
                    acceptat = True
                    break
            return acceptat
        else:
            for state in transitions[current_state][nfa[count]]:
                gasit = cautare(count + 1, state, max_size)
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