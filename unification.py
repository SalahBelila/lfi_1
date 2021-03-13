def unify(term_1, term_2):
    term_1 = term_1.replace(' ', '')
    term_2 = term_2.replace(' ', '')
    if is_idf(term_1) or is_const(term_1) or is_idf(term_2) or is_const(term_2):
        if term_1 == term_2:
            return set()
        elif is_idf(term_1):
            if term_1 in term_2:
                return None
            else:
                return (term_2, term_1)
        elif is_idf(term_2):
            if term_2 in term_1:
                return None
            else:
                return (term_1, term_2)
        else:
            return None
    if is_function(term_1) and is_function(term_2):
        broken_1 = break_up(term_1)
        broken_2 = break_up(term_2)
        if (broken_1['name'] == broken_2['name']) and (len(broken_1['args']) == len(broken_2['args'])):
            subs = []
            for i in range(len(broken_1['args'])):
                sub = unify(broken_1['args'][i], broken_2['args'][i])
                if sub == None:
                    return None
                if not(sub == set()):
                    broken_1['args'] = broken_1['args'][:i] + apply_sub(broken_1['args'][i:], sub)
                    broken_2['args'] = broken_2['args'][:i] + apply_sub(broken_2['args'][i:], sub)
                    subs.append(sub)
            return subs
        else:
            return None
    pass

def apply_sub(term, sub):
    result = []
    for arg in term:
        result.append(arg.replace(sub[0], sub[1]))
    return result

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
            current_arg += args[i]
            if args[i] == '(':
                i += 1
                while i < len(args) and not(args[i] == ')'):
                    current_arg += args[i]
                    i += 1
                if args[i] == ')':
                    current_arg += ')'
            i += 1
        args_list.append(current_arg)
        i += 1

    return {'name': function_name, 'args': args_list}
    

def is_function(function):
    function = list(function)
    function_name = ''
    for c in function:
        if (c == '('):
            break
        function_name += c
    return is_idf(function_name) and function[-1] == ')'

def is_idf(idf):
    idf = list(idf)
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
    if const[0] == '"' and const[-1] == '"':
        return True
    else:
        for c in const:
            if 47 < ord(c) < 58:
                continue
            else:
                return False
        return True