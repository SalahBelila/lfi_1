from resolution import Clause, resolve, clausal_set, clausal_set_union
from complete_strategy import complete_strategy, reduce
from unification import  unify
from pretty import stringify
import gc

# set_1 = clausal_set('a + b,a + -b,-a + b,-a + -b')
# result = complete_strategy(set_1)
# result['visuals'].finish()

# 'p(f(a), g(Y))', 'p(X, X)'
# 'p(b, X, f(g(Z)))', 'p(Z, f(Y), f(Y))'

# term_1 = 'p (Z, f(Z))'
# term_2 = 'p (X, X)'
# print(unify(term_1, term_2))

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

        '''
    else:
        return None

def main_start(can_exit=False):
    while not can_exit:
        gc.collect()
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
        print('2- Get all resolvents of two clausal sets.')
        print('3- Reduce a clausal set.')
        print('4- Return to Main Menu.')
        print('5- Exit.')

        choice = input()

        if choice == '1':
            clause_1 = Clause(input('Enter the first Clause: '))
            clause_2 = Clause(input('Enter the second Clause: '))
            print('Result:-\t( ', clause_1 / clause_2, ' )')
        elif choice == '2':
            set_1 = input('Enter the first clausal set: ')
            set_2 = input('Enter the second clausal set: ')
            print('Result:-\t{ ', stringify(resolve(clausal_set(set_1), clausal_set(set_2))), ' }')
        elif choice == '3':
            set_1 = input('Enter a clausal set to be reduced: ')
            print('Result:-\t{ ', stringify(reduce(clausal_set(set_1))), ' }')
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
        print('Enter two clausal sets to apply the complete strategy algorithm on.')
        set_1 = input('Enter the first clausal set: ')
        set_2 = input('Enter the second clausal set: ')
        choice = input('Be verbose?[Y/N]: ')
        result = complete_strategy(clausal_set(set_1), clausal_set(set_2))
        if choice == 'y' or choice == 'Y':
            result['visuals'].finish()
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
        term_2 = input('Enter the second term: ')
        result = unify(term_1, term_2)
        print('Result:- \tO =', stringify(result) if result is not None else '')

        choice = input('Press c to return to Main Menu, or press any other key to exit: ')
        if choice == 'c' or choice == 'C':
            return False
        else:
            return True

main_start()
