class Literal:
    def __init__(self, term_string):
        temp_term = term_string.split('-')
        if (len(temp_term) == 2):
            self.term = temp_term[1]
            self.is_negated = (temp_term[0] == '')
        else:
            self.term = temp_term[0]
            self.is_negated = False
        pass
    
    def __str__(self):
        return '-'+self.term if self.is_negated else self.term
    
class Clause:
    def __init__(self, clause_string):
        self.is_empty = False
        temp_term_list = clause_string.replace('(', '').replace(')', '').replace(' ', '').split('+')
        if len(temp_term_list) == 1 and temp_term_list[0] == '':
            self.is_empty = True
        self.terms = set([Literal(term) for term in temp_term_list])
        pass
        
    def __truediv__(self, clause):
        removed = set()
        for self_term in self.terms:
            for term in clause.terms:
                if (self_term.term == term.term) and not(term.is_negated == self_term.is_negated):
                    removed.add(term.term)
        result_string = set()
        for term in self.terms.union(clause.terms):
            if not(term.term in removed):
                new_term_string = '-'+term.term if term.is_negated else term.term
                result_string.add(new_term_string)
        result_string = '+'.join(result_string)
        if len(removed) == 0:
            return None
        else:
            return Clause(result_string)
    
    def is_tautology(self):
        for term_1 in self.terms:
            for term_2 in self.terms:
                if (term_1.term == term_2.term) and not(term_1.is_negated == term_2.is_negated):
                    return True
        return False
    
    def includes(self, clause):
        occurences = 0
        for term_1 in clause.terms:
            for term_2 in self.terms:
                if (term_1.term == term_2.term) and (term_1.is_negated == term_2.is_negated):
                    occurences += 1
                    break
        return occurences >= len(clause.terms)

    def __str__(self):
        if self.is_empty:
            return '⊥'
        else:
            return '+'.join([term.__str__() for term in self.terms])

def resolve(set_1, set_2):
    result = []
    for clause_1 in set_1:
        for clause_2 in set_2:
            resolvent = clause_1 / clause_2
            if not (resolvent == None):
                result.append(resolvent.__str__())
    return clausal_set(','.join(result))

def clausal_set(string_clauses):
    if len(string_clauses) == 0:
        return set()
    else:
        string_clauses = string_clauses.replace(' ', '')
        return set([Clause(unique_clause) for unique_clause in set([clause for clause in string_clauses.split(',')])])

def clausal_set_union(set_1, set_2):
    set_1_string = ','.join([str(clause) for clause in set_1])
    set_2_string = ','.join([str(clause) for clause in set_2])
    return clausal_set(set_1_string+','+set_2_string)