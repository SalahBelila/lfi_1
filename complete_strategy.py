from resolution import resolve, clausal_set_union, clausal_set
from pretty import PrettyTable

def complete_strategy(c_set, max_iterations=20):
    #1 Initialization
    delta = reduce(c_set)
    theta = set()
    d_U_t = None
    resolvents = None
    i = 0
    pt = PrettyTable(['k', 'Delta', 'Theta', 'Delta U Theta', 'R(Delta and Delta U Theta)'], enum_col=0)
    while (len(delta) > 0):
        #2 Calculate new Delta
        #2.a
        d_U_t = clausal_set_union(delta, theta)
        resolvents = clausal_set_union(resolve(delta), resolve(d_U_t))
        reduced_resolvents = reduce(resolvents)
        #2.b
        to_be_removed = set()
        for clause_1 in reduced_resolvents:
            for clause_2 in d_U_t:
                if clause_1.includes(clause_2):
                    to_be_removed.add(clause_1)
                    break
        new_delta = reduced_resolvents - to_be_removed

        #3 Calcualte new Theta
        to_be_removed = set()
        for clause_1 in d_U_t:
            for clause_2 in new_delta:
                if clause_1.includes(clause_2):
                    to_be_removed.add(clause_1)
                    break
        new_theta = d_U_t - to_be_removed

        pt.add([str(i), [str(c) for c in delta], [str(c) for c in theta], [str(c) for c in d_U_t], [str(c) for c in resolvents]])

        delta = new_delta
        theta = new_theta
        resolvents = reduced_resolvents
        i += 1

    pt.add([str(i), [str(c) for c in delta], [str(c) for c in theta], [str(c) for c in d_U_t], [str(c) for c in resolvents]])
    return {'delta': delta, 'theta': theta, 'visuals': pt}
    
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