class PrettyTable:
    def __init__(self, headers_list):
        self.headers_list = headers_list
        self.widths = [0]*len(headers_list)
        self.data = [headers_list]
        pass

    def __init(self, headers_list, data):
        self.__init__(headers_list)
        for d in data:
            self.add(d)

    def add(self, data_iterable):
        assert(len(data_iterable) == len(self.headers_list))
        temp = []
        for i in range(len(data_iterable)):
            string = stringify(data_iterable[i])
            temp.append(string)
            if self.widths[i] < len(string):
                self.widths[i] = len(string) 
        self.data.append(temp)
    
    def finish(self):
        for strings in self.data:
            for _ in range(sum(self.widths)+2*len(self.widths)):
                print('-', end='')
            print('\n')

            for i in range(len(self.widths)):
                white_space = self.widths[i] - len(strings[i])
                leading_space = white_space // 2
                remainder_space = white_space - leading_space
                print('|', end='')
                for _ in range(leading_space):
                    print(' ', end='')
                print(strings[i], end='')
                for _ in range(remainder_space):
                    print(' ', end='')
                print('|', end='')
            print('\n')

def stringify(iter_list):
    iter_list = [str(e) for e in iter_list]
    return ' {' + ', '.join(iter_list) + '} '