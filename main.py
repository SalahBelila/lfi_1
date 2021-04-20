from resolution import Clause, resolve, clausal_set, clausal_set_union
from complete_strategy import complete_strategy, reduce
from unification import  unify
from pretty import stringify
from checker import analyze_term, analyze_clause, analyze_clausal_set

# a + b + -a, a + b, a + b + c, a + -b, -a + b, -a + -b

def usage(choice):
    if choice == 1:
        return '''
            How to write a clause:
                example 1: a+b+-c, example 2: a + b + (-c)
                '-': the negation.
                '+': the OR operand.
        '''
    elif choice == 2:
        return '''
            How to write a clausal set:
                example 1: ((a + b), a + -b, (c + b))
                Parantheses can be omitted.
        '''
    elif choice == 3:
        return '''
            How to write terms:
                a term can be a constant, variable or function.
                a constant is either a number or a double quoted text ("text")
                a variable is an IDF.
                a function is of the form IDF(term1, term2, ..., termx)
                where IDF is a word that contains only numbers, letters and underscores and does not start with a number.
                example 1: p(x, f(z), "a"), example 2: g(7, f(x), h(k(z)), "7")
        '''
    else:
        return None

def main_start(can_exit=False):
    while not can_exit:
        print('MAIN MENU')
        print('1- Resolution.')
        print('2- Complete Strategy.')
        print('3- Unification.')
        print('4- Help.')
        print('5- Exit.')

        choice = input('Pick a Choice: ')

        if choice == '1':
            can_exit = resolution()
        elif choice == '2':
            can_exit = c_strategy()
        elif choice == '3':
            can_exit = unification()
        elif choice == '4':
            i = 1
            while usage(i) is not None:
                print(usage(i))
                i += 1
        elif choice == '5':
            print('GOOD BYE.')
            break
        else:
            print('Invalid option.')

def resolution():
    while True:
        print('Resolution Menu.')
        print('Pick a Choice.')
        print('1- Resolve two clauses.')
        print('2- Get all resolvents of a clausal set.')
        print('3- Reduce a clausal set.')
        print('4- Return to Main Menu.')
        print('5- Exit.')

        choice = input()

        if choice == '1':
            clause_1 = Clause(input('Enter the first Clause: '))
            if not analyze_clause(str(clause_1)):
                print('invalid clause, please try again.')
                continue
            clause_2 = Clause(input('Enter the second Clause: '))
            if not analyze_clause(str(clause_2)):
                print('invalid clause, please try again.')
                continue
            print('Result:-\t( ', clause_1 // clause_2, ' )')
        
        elif choice == '2':
            set_1 = input('Enter the clausal set: ')
            if not analyze_clausal_set(set_1):
                print('invalid clausal set, please try again.')
                continue
            print('Result:-\t', stringify(resolve(clausal_set(set_1))))

        elif choice == '3':
            set_1 = input('Enter a clausal set to be reduced: ')
            if not analyze_clausal_set(set_1):
                print('invalid clausal set, please try again.')
                continue
            print('Result:-\t', stringify(reduce(clausal_set(set_1))))

        elif choice == '4':
            break
        elif choice == '5':
            print('GOOD BYE.')
            return True
        else:
            print('Invalid option.')

        input('Press any key to continue...')

def c_strategy():
    while True:
        print('Enter a clausal set to apply the complete strategy algorithm on.')
        set_1 = input('Enter the clausal set: ')
        choice = input('Be verbose? [Y/N]: ')
        result = complete_strategy(clausal_set(set_1))
        if choice == 'y' or choice == 'Y':
            print('\n\n')
            result['visuals'].finish(inline_border=False)
        else:
            print('Result:-\n\tDelta: ', stringify(result['delta']), '\n\tTheta: ', stringify(result['theta']))

        choice = input('Press c to return to Main Menu, or press any other key to exit: ')
        if choice == 'c' or choice == 'C':
            return False
        else:
            return True

def unification():
    while True:
        print('Enter two terms.')
        term_1 = input('Enter the first term: ')
        result = analyze_term(term_1, [])
        if not result[0]:
            print('invalid term, please try again.')
            print(result[1])
            print('press a key to continue')
            input()
            continue

        term_2 = input('Enter the second term: ')
        analyze_term(term_2, [])
        if not result[0]:
            print('invalid term, please try again.')
            print(result[1])
            print('press a key to continue')
            input()
            continue

        result = unify(term_1, term_2, [])
        print('Result:- \tO = ' + stringify(result) if result is not None else 'Unification Failed.')
        print('Note: the pair (x, y) is read as: substitute every occurence of y by x.')
        choice = input('Press c to return to Main Menu, or press any other key to exit: ')
        if choice == 'c' or choice == 'C':
            return False
        else:
            return True

if __name__ == '__main__':
    main_start()
