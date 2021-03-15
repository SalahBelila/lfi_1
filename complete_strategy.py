from resolution import resolve, clausal_set_union
from pretty import PrettyTable

def complete_strategy(clausal_set, activate_visuals=False):
    #1 Initialization
    delta = reduce(clausal_set)
    theta = set()
    pp = PrettyTable(['Delta', 'Theta'])
    pp.add([[str(d) for d in delta], [str(t) for t in theta]])
    # print('|Delta:-', [str(d) for d in delta], ' |Theta:-', [str(t) for t in theta], ' |')
    while len(delta) > 0:
        #2 calculate new delta
        #2.a
        delta_U_theta = clausal_set_union(delta, theta)
        candidate_delta = reduce(resolve(delta, delta_U_theta))
        #2.b
        to_be_removed = set()
        for clause_1 in candidate_delta:
            for clause_2 in delta_U_theta:
                if clause_1.includes(clause_2):
                    to_be_removed.add(clause_1)
                    break
        delta = candidate_delta - to_be_removed

        #3 calculate the new theta
        to_be_removed = set()
        for clause_1 in delta_U_theta:
            for clause_2 in delta:
                if clause_1.includes(clause_2):
                    to_be_removed.add(clause_1)
        theta = delta_U_theta - to_be_removed
        pp.add([[str(d) for d in delta], [str(t) for t in theta]])
        # print('|Delta:-', [str(d) for d in delta], ' |Theta:-', [str(t) for t in theta], ' |')
    return {'delta': delta, 'theta': theta, 'visuals': pp}
    
def reduce(clausal_set):
    to_be_removed = set()
    for clause_1 in clausal_set:
        if clause_1.is_tautology():
            to_be_removed.add(clause_1)
            continue
        for clause_2 in clausal_set:
            if clause_1.includes(clause_2) and not(clause_1 == clause_2):
                to_be_removed.add(clause_1)
                break
    return clausal_set - to_be_removed