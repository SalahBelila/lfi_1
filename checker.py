def analyze_term(term, result):
    term = term.replace(' ', '')
    if is_idf(term):
        result.append((term, 'variable'))
        return result
    elif is_const(term):
        result.append((term, 'constant'))
        return result
    elif is_function(term):
        broke = break_up(term)
        result.append((broke['name'], 'function'))
        for t in broke['args']:
            value = analyze_term(t, result)
            if len(value) == 2 and value[0] == False:
                result.append((t, 'Error'))
                break
        if len(result) > 0 and result[-1][1] == 'Error':
            return (False, filter_duplication(result))
        else:
            return (True, filter_duplication(result))
    else:
        return (False, term)
    
def analyze_clause(clause):
    clause = clause.replace(' ', '').replace(')', '').replace('(', '').split('+')
    for c in clause:
        c = list(c)
        if len(c) == 2:
            if c[0] == '-' and ((64 < ord(c[1]) < 91) or (96 < ord(c[1]) < 123)):
                continue
            else:
                return False
        elif len(c) == 1:
            if (64 < ord(c[0]) < 91) or (96 < ord(c[0]) < 123):
                continue
            else:
                return False
        else:
            return False
    return True

def analyze_clausal_set(c_set):
    c_set = c_set.replace(' ', '').replace(')', '').replace('(', '').split(',')
    for c in c_set:
        if analyze_clause(c):
            continue
        else:
            return False
    return True

def break_up(function):
    function = list(function)
    function_name = ''
    for c in function:
        if c == '(':
            break
        function_name += c
    args = function[len(function_name) + 1:-1]
    args_list = []
    i = 0
    while i < len(args):
        current_arg = ''
        while i < len(args) and not(args[i] == ','):
            if args[i] == '(':
                opened = -1
                while i < len(args) and not(opened == 0):
                    if opened == -1:
                        opened = 0
                    if args[i] == '(':
                        opened += 1
                    if args[i] == ')':
                        opened -= 1
                    current_arg += args[i]
                    i += 1
            else:
                current_arg += args[i]
                i += 1
        args_list.append(current_arg)
        i += 1

    return {'name': function_name, 'args': args_list}
    

def is_function(function):
    function = list(function)
    if len(function) == 0:
        return False
    function_name = ''
    for c in function:
        if (c == '('):
            break
        function_name += c
    space_free = ''.join(function).replace(' ', '')
    result = (is_idf(function_name) and function[-1] == ')') and (',,' not in space_free) and ('(,' not in space_free) and (',)' not in space_free)
    return result

def is_idf(idf):
    idf = list(idf)
    if len(idf) == 0:
        return False
    if (64 < ord(idf[0]) < 91) or (96 < ord(idf[0]) < 123):
        for c in idf:
            if (64 < ord(c) < 91) or (96 < ord(c) < 123) or (47 < ord(c) < 58) or (c == '_'):
                continue
            else:
                return False
        return True
    else:
        return False

def is_const(const):
    const = list(const)
    if len(const) == 0:
        return False
    if const[0] == '"' and const[-1] == '"':
        return True
    else:
        for c in const:
            if 47 < ord(c) < 58:
                continue
            else:
                return False
        return True

def filter_duplication(iterable_of_two_element_tuples):
    result = []
    for t in iterable_of_two_element_tuples:
        if exists_in(result, t):
            continue
        else:
            result.append(t)
    return result

def exists_in(iterable_of_two_element_tuples, two_element_tuple):
    for t in iterable_of_two_element_tuples:
        if (t[0] == two_element_tuple[0]) and (t[1] == two_element_tuple[1]):
            return True
    return False