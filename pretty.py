class PrettyTable:
    def __init__(self, headers_list, enum_col=None):
        self.headers_list = headers_list
        self.widths = [0]*len(headers_list)
        self.data = [headers_list]
        self.enum_col = enum_col
        for i in range(len(self.widths)):
            self.widths[i] = len(self.headers_list[i])
        pass

    def __init(self, headers_list, data):
        self.__init__(headers_list)
        for d in data:
            self.add(d)

    def add(self, data_iterable):
        assert(len(data_iterable) == len(self.headers_list))
        temp = []
        for i in range(len(data_iterable)):
            string = stringify(data_iterable[i], non_set=(i == self.enum_col))
            temp.append(string)
            if self.widths[i] < len(string):
                self.widths[i] = len(string) 
        self.data.append(temp)
    
    def finish(self, inline_border=False):
        for strings in self.data:
            if inline_border == True:
                for _ in range(sum(self.widths)+2*len(self.widths) - 1):
                    print('-', end='')
                print('\n')

            print(' |', end='')
            for i in range(len(self.widths)):
                white_space = self.widths[i] - len(strings[i])
                leading_space = white_space // 2
                remainder_space = white_space - leading_space
                for _ in range(leading_space):
                    print(' ', end='')
                print(strings[i], end='')
                for _ in range(remainder_space):
                    print(' ', end='')
                print('|', end='')
            print('\n')

def stringify(iter_list, non_set=False):
    if len(iter_list) == 0:
        return '{}'
    if non_set == True:
        return f' {str(iter_list)} '
    iter_list = [str(e) for e in iter_list]
    return '{ ' + ', '.join(iter_list) + ' }'