from resolution import Clause, resolve, clausal_set, clausal_set_union
from complete_strategy import complete_strategy

set_1 = clausal_set('a + b,a + -b,-a + b,-a + -b')
result = complete_strategy(set_1)
print('Delta:------- ', len(result['delta']))
for c in result['delta']:
    print(c)
print('Theta:-------', len(result['theta']))
for c in result['theta']:
    print(c)