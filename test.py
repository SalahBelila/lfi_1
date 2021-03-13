from resolution import Clause, resolve, clausal_set, clausal_set_union
from complete_strategy import complete_strategy
from unification import  unify

# set_1 = clausal_set('a + b,a + -b,-a + b,-a + -b')
# result = complete_strategy(set_1)
# print('Delta:------- ', len(result['delta']))
# for c in result['delta']:
#     print(c)
# print('Theta:-------', len(result['theta']))
# for c in result['theta']:
#     print(c)

term_1 = 'p(b,X,f(g(Z)))'
term_2 = 'p(Z,f(Y),f(Y))'
print(unify(term_1, term_2))