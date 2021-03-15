class Literal:
    def __init__(self, literal_string):
        temp_literal = literal_string.split('-')
        if (len(temp_literal) == 2):
            self.literal = temp_literal[1]
            self.is_negated = (temp_literal[0] == '')
        else:
            self.literal = temp_literal[0]
            self.is_negated = False
        pass
    
    def __str__(self):
        return '-'+self.literal if self.is_negated else self.literal
    
class Clause:
    def __init__(self, clause_string):
        self.is_empty = False
        temp_literal_list = clause_string.replace('(', '').replace(')', '').replace(' ', '').split('+')
        if len(temp_literal_list) == 1 and temp_literal_list[0] == '':
            self.is_empty = True
        self.literals = set([Literal(literal) for literal in temp_literal_list])
        pass
        
    def __truediv__(self, clause):
        removed = set()
        for self_literal in self.literals:
            for literal in clause.literals:
                if (self_literal.literal == literal.literal) and not(literal.is_negated == self_literal.is_negated):
                    removed.add(literal.literal)
        result_string = set()
        for literal in self.literals.union(clause.literals):
            if not(literal.literal in removed):
                new_literal_string = '-'+literal.literal if literal.is_negated else literal.literal
                result_string.add(new_literal_string)
        result_string = '+'.join(result_string)
        if len(removed) == 0:
            return None
        else:
            return Clause(result_string)
    
    def is_tautology(self):
        for literal_1 in self.literals:
            for literal_2 in self.literals:
                if (literal_1.literal == literal_2.literal) and not(literal_1.is_negated == literal_2.is_negated):
                    return True
        return False
    
    def includes(self, clause):
        occurences = 0
        for literal_1 in clause.literals:
            for literal_2 in self.literals:
                if (literal_1.literal == literal_2.literal) and (literal_1.is_negated == literal_2.is_negated):
                    occurences += 1
                    break
        return occurences >= len(clause.literals)

    def __str__(self):
        if self.is_empty:
            return '⊥'
        else:
            return '+'.join([literal.__str__() for literal in self.literals])

def resolve(set_1, set_2):
    result = []
    for clause_1 in set_1:
        for clause_2 in set_2:
            resolvent = clause_1 / clause_2
            if not (resolvent == None):
                result.append(resolvent.__str__())
    return clausal_set(', '.join(result))

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