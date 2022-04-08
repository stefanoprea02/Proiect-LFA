import nfa_parser_engine
import sys

if(sys.argv[0] == "nfa_acceptance_engine.py"):
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

    #cautam daca exista un nod care pleaca din nodul curent prin valoare din string
    #daca da verificam daca am ajuns la finalul string-ului
    #ca sa verificam daca nodul se afla in nodurile finale
    #daca nu am ajuns la final trecem la urmatorul nod prin apelarea functiei

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